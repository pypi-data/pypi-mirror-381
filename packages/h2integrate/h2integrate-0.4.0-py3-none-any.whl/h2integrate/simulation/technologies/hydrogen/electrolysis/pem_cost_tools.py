import numpy as np
from attrs import field, define

from h2integrate.tools.profast_tools import create_years_of_operation


@define
class ElectrolyzerLCOHInputConfig:
    """Calculates inputs for LCOH functions related to electrolyzer
        performance outside of capex and opex.

    Args:
        electrolyzer_physics_results (dict): results from run_electrolyzer_physics()
        electrolyzer_config (dict): sub-dictionary of h2integrate_config
        financial_analysis_start_year (int): analysis start year
        installation_period_months (int|float|None): installation period in months. defaults to 36.
    """

    electrolyzer_physics_results: dict
    electrolyzer_config: dict
    financial_analysis_start_year: int
    installation_period_months: int | float | None = field(default=36)

    electrolyzer_capacity_kW: int | float = field(init=False)
    project_lifetime_years: int = field(init=False)
    long_term_utilization: dict = field(init=False)
    rated_capacity_kg_pr_day: float = field(init=False)
    water_usage_gal_pr_kg: float = field(init=False)

    electrolyzer_annual_energy_usage_kWh: list[float] = field(init=False)
    electrolyzer_eff_kWh_pr_kg: list[float] = field(init=False)
    electrolyzer_annual_h2_production_kg: list[float] = field(init=False)

    refurb_cost_percent: list[float] = field(init=False)
    replacement_schedule: list[float] = field(init=False)

    def __attrs_post_init__(self):
        annual_performance = self.electrolyzer_physics_results["H2_Results"][
            "Performance Schedules"
        ]

        #: electrolyzer system capacity in kW
        self.electrolyzer_capacity_kW = self.electrolyzer_physics_results["H2_Results"][
            "system capacity [kW]"
        ]

        #: int: lifetime of project in years
        self.project_lifetime_years = len(annual_performance)

        #: float: electrolyzer beginnning-of-life rated H2 production capacity in kg/day
        self.rated_capacity_kg_pr_day = (
            self.electrolyzer_physics_results["H2_Results"]["Rated BOL: H2 Production [kg/hr]"] * 24
        )

        #: float: water usage in gallons of water per kg of H2
        self.water_usage_gal_pr_kg = self.electrolyzer_physics_results["H2_Results"][
            "Rated BOL: Gal H2O per kg-H2"
        ]
        #: list(float): annual energy consumed by electrolyzer per year of operation in kWh/year
        self.electrolyzer_annual_energy_usage_kWh = annual_performance[
            "Annual Energy Used [kWh/year]"
        ].to_list()
        #: list(float): annual avg efficiency of electrolyzer for each year of operation in kWh/kg
        self.electrolyzer_eff_kWh_pr_kg = annual_performance[
            "Annual Average Efficiency [kWh/kg]"
        ].to_list()
        #: list(float): annual hydrogen production for each year of operation in kg/year
        self.electrolyzer_annual_h2_production_kg = annual_performance[
            "Annual H2 Production [kg/year]"
        ]
        #: dict: annual capacity factor of electrolyzer for each year of operation
        self.long_term_utilization = self.make_lifetime_utilization()

        use_complex_refurb = False
        if "complex_refurb" in self.electrolyzer_config.keys():
            if self.electrolyzer_config["complex_refurb"]:
                use_complex_refurb = True

        # complex schedule assumes stacks are replaced in the year they reach end-of-life
        if use_complex_refurb:
            self.replacement_schedule = self.calc_complex_refurb_schedule()
            self.refurb_cost_percent = list(
                np.array(
                    self.replacement_schedule * self.electrolyzer_config["replacement_cost_percent"]
                )
            )

        # simple schedule assumes all stacks are replaced in the same year
        else:
            self.replacement_schedule = self.calc_simple_refurb_schedule()
            self.refurb_cost_percent = list(
                np.array(
                    self.replacement_schedule * self.electrolyzer_config["replacement_cost_percent"]
                )
            )

    def calc_simple_refurb_schedule(self):
        """Calculate electrolyzer refurbishment schedule
            assuming that all stacks are replaced in the same year.

        Returns:
            list: list of years when stacks are replaced.
            a value of 1 means stacks are replaced that year.
        """
        annual_performance = self.electrolyzer_physics_results["H2_Results"][
            "Performance Schedules"
        ]
        refurb_simple = np.zeros(len(annual_performance))
        refurb_period = int(
            round(
                self.electrolyzer_physics_results["H2_Results"]["Time Until Replacement [hrs]"]
                / 8760
            )
        )
        refurb_simple[refurb_period : len(annual_performance) : refurb_period] = 1.0

        return refurb_simple

    def calc_complex_refurb_schedule(self):
        """Calculate electrolyzer refurbishment schedule
            stacks are replaced in the year they reach EOL.

        Returns:
            list: list of years when stacks are replaced. values are are fraction of
            the total installed capacity.
        """
        annual_performance = self.electrolyzer_physics_results["H2_Results"][
            "Performance Schedules"
        ]
        refurb_complex = annual_performance["Refurbishment Schedule [MW replaced/year]"].values / (
            self.electrolyzer_capacity_kW / 1e3
        )
        return refurb_complex

    def make_lifetime_utilization(self):
        """Make long term utilization dictionary for electrolyzer system.

        Returns:
            dict: keys are years of operation and values are the capacity factor for that year.
        """
        annual_performance = self.electrolyzer_physics_results["H2_Results"][
            "Performance Schedules"
        ]

        years_of_operation = create_years_of_operation(
            self.project_lifetime_years,
            self.financial_analysis_start_year,
            self.installation_period_months,
        )

        cf_per_year = annual_performance["Capacity Factor [-]"].to_list()
        utilization_dict = dict(zip(years_of_operation, cf_per_year))
        return utilization_dict


def calc_electrolyzer_variable_om(electrolyzer_physics_results, h2integrate_config):
    """Calculate variable O&M of electrolyzer system in $/kg-H2.

    Args:
        electrolyzer_physics_results (dict): results from run_electrolyzer_physics()
        h2integrate_config (:obj:`h2integrate_simulation.H2IntegrateSimulationConfig`): h2integrate
            simulation config.

    Returns:
        dict | float: electrolyzer variable o&m in $/kg-H2.
    """
    electrolyzer_config = h2integrate_config["electrolyzer"]
    annual_performance = electrolyzer_physics_results["H2_Results"]["Performance Schedules"]

    if "var_om" in electrolyzer_config.keys():
        electrolyzer_vopex_pr_kg = (
            electrolyzer_config["var_om"]
            * annual_performance["Annual Average Efficiency [kWh/kg]"].values
        )

        if "financial_analysis_start_year" not in h2integrate_config["finance_parameters"]:
            financial_analysis_start_year = h2integrate_config["project_parameters"][
                "financial_analysis_start_year"
            ]
        else:
            financial_analysis_start_year = h2integrate_config["finance_parameters"][
                "financial_analysis_start_year"
            ]
        if "installation_time" not in h2integrate_config["project_parameters"]:
            installation_period_months = 36
        else:
            installation_period_months = h2integrate_config["project_parameters"][
                "installation_time"
            ]

        years_of_operation = create_years_of_operation(
            h2integrate_config["project_parameters"]["project_lifetime"],
            financial_analysis_start_year,
            installation_period_months,
        )
        # $/kg-year
        vopex_elec = dict(zip(years_of_operation, electrolyzer_vopex_pr_kg))

    else:
        vopex_elec = 0.0
    return vopex_elec
