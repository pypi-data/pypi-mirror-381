from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import ProFAST  # system financial model
import numpy_financial as npf
from attrs import field, define
from ORBIT import ProjectManager
from hopp.simulation import HoppInterface


def adjust_dollar_year(init_cost, init_dollar_year, adj_cost_year, costing_general_inflation):
    """Adjust cost based on inflation.

    Args:
        init_cost (dict, float, int, list, np.ndarrray): cost of item ($)
        init_dollar_year (int): dollar-year of init_cost
        adj_cost_year (int): dollar-year to adjust cost to
        costing_general_inflation (float): inflation rate (%)

    Returns:
        same type as init_cost: cost in dollar-year of adj_cost_year
    """
    periods = adj_cost_year - init_dollar_year
    if isinstance(init_cost, (float, int)):
        adj_cost = -npf.fv(costing_general_inflation, periods, 0.0, init_cost)
    elif isinstance(init_cost, dict):
        adj_cost = {}
        for key, val in init_cost.items():
            new_val = -npf.fv(costing_general_inflation, periods, 0.0, val)
            adj_cost.update({key: new_val})
    elif isinstance(init_cost, (list, np.ndarray)):
        adj_cost = np.zeros(len(init_cost))
        for i in range(len(init_cost)):
            adj_cost[i] = -npf.fv(costing_general_inflation, periods, 0.0, init_cost[i])
        if isinstance(init_cost, list):
            adj_cost = list(adj_cost)

    return adj_cost


@define
class WindCostConfig:
    """
    Represents the inputs to the wind cost models

    Attributes:
        design_scenario (Dict[str, str]):
            Definition of plant subsystem locations (e.g. onshore platform, offshore, none, etc)
        hopp_config (Dict[str, float]):
            Configuration parameters for HOPP
        h2integrate_config (Dict[str, float]):
            Configuration parameters for H2Integrate
        orbit_config (Dict[str, float], optional):
            Required input structure for ORBIT
        turbine_config (Dict[str, float], optional):
            Configuration parameters specific to turbine
        orbit_hybrid_electrical_export_config (Dict[str, float], optional):
            Configuration parameters for hybrid electrical export in ORBIT, required if using a
            different substation size for the hybrid plant than for the wind plant alone
        weather (Union[list, tuple, numpy.ndarray], optional):
            Array-like of wind speeds for ORBIT to use in determining installation time and costs
    """

    design_scenario: dict[str, str]
    hopp_config: dict[str, float]
    h2integrate_config: dict[str, float]
    orbit_config: dict[str, float] | None = field(default={})
    turbine_config: dict[str, float] | None = field(default={})
    orbit_hybrid_electrical_export_config: dict[str, float] | None = field(default={})
    weather: list | tuple | np.ndarray | None = field(default=None)
    hopp_interface: HoppInterface | None = field(default=None)


@define
class WindCostOutputs:
    """
    Represents the outputs to the wind cost models.

    Attributes:
        total_wind_cost_no_export (float):
            Total wind cost without export system costs
        total_used_export_system_costs (float):
            Total used export system costs
        annual_operating_cost_wind (float):
            Annual operating cost for wind
        installation_time (float, optional):
            Estimated installation time in months (default: 0.0)
        orbit_project (dict, optional):
            Details of the ORBIT project (default: None)
    """

    total_wind_cost_no_export: float
    annual_operating_cost_wind: float
    installation_time: float = field(default=0.0)
    total_used_export_system_costs: float | None = field(default=0.0)
    orbit_project: dict | ProjectManager | None = field(default=None)


def run_wind_cost_model(wind_cost_inputs: WindCostConfig, verbose=False) -> WindCostOutputs:
    if wind_cost_inputs.design_scenario["wind_location"] == "offshore":
        # if per kw
        project, orbit_hybrid_electrical_export_project = run_orbit(
            wind_cost_inputs.orbit_config,
            verbose=verbose,
            weather=wind_cost_inputs.weather,
            orbit_hybrid_electrical_export_config=wind_cost_inputs.orbit_hybrid_electrical_export_config,
        )

        (
            total_wind_cost_no_export,
            total_used_export_system_costs,
        ) = breakout_export_costs_from_orbit_results(
            project,
            wind_cost_inputs.h2integrate_config,
            wind_cost_inputs.design_scenario,
        )

        if orbit_hybrid_electrical_export_project is not None:
            (
                _,
                total_used_export_system_costs,
            ) = breakout_export_costs_from_orbit_results(
                orbit_hybrid_electrical_export_project,
                wind_cost_inputs.h2integrate_config,
                wind_cost_inputs.design_scenario,
            )

        # WIND ONLY Total O&M expenses including fixed, variable, and capacity-based, $/year
        # use values from hybrid substation if a hybrid plant
        if orbit_hybrid_electrical_export_project is None:
            annual_operating_cost_wind = (
                max(project.monthly_opex.values()) * 12
            )  # np.average(hopp_results["hybrid_plant"].wind.om_total_expense)

        else:
            annual_operating_cost_wind = (
                max(orbit_hybrid_electrical_export_project.monthly_opex.values()) * 12
            )

        if "installation_time" in wind_cost_inputs.h2integrate_config["project_parameters"]:
            installation_time = wind_cost_inputs.h2integrate_config["project_parameters"][
                "installation_time"
            ]
        else:
            installation_time = (project.installation_time / (365 * 24)) * (12.0 / 1.0)

        # if total amount
        # TODO
        return WindCostOutputs(
            total_wind_cost_no_export=total_wind_cost_no_export,
            total_used_export_system_costs=total_used_export_system_costs,
            annual_operating_cost_wind=annual_operating_cost_wind,
            installation_time=installation_time,
            orbit_project=project,
        )
    elif wind_cost_inputs.design_scenario["wind_location"] == "onshore":
        total_wind_cost_no_export = (
            wind_cost_inputs.hopp_config["config"]["cost_info"]["wind_installed_cost_mw"]
            * wind_cost_inputs.hopp_config["technologies"]["wind"]["num_turbines"]
            * wind_cost_inputs.turbine_config["turbine_rating"]
        )

        annual_operating_cost_wind = wind_cost_inputs.hopp_interface.system.wind.om_total_expense[0]

        if "installation_time" in wind_cost_inputs.h2integrate_config["project_parameters"]:
            installation_time = wind_cost_inputs.h2integrate_config["project_parameters"][
                "installation_time"
            ]
        else:
            installation_time = 0

        return WindCostOutputs(
            total_wind_cost_no_export=total_wind_cost_no_export,
            annual_operating_cost_wind=annual_operating_cost_wind,
            installation_time=installation_time,
        )
    else:
        raise ValueError(
            "Wind design location must either be 'onshore' or 'offshore', but currently "
            f"'wind_location' is set to {wind_cost_inputs.design_scenario['wind_location']}."
        )


# Function to run orbit from provided inputs - this is just for wind costs
def run_orbit(orbit_config, verbose=False, weather=None, orbit_hybrid_electrical_export_config={}):
    # set up ORBIT
    project = ProjectManager(orbit_config, weather=weather)

    # run ORBIT
    project.run(availability=orbit_config["installation_availability"])

    # run ORBIT for hybrid substation if applicable
    if orbit_hybrid_electrical_export_config == {}:
        hybrid_substation_project = None
    else:
        hybrid_substation_project = ProjectManager(
            orbit_hybrid_electrical_export_config, weather=weather
        )
        hybrid_substation_project.run(availability=orbit_config["installation_availability"])

    # print results if desired
    if verbose:
        print(f"Installation CapEx:  {project.installation_capex/1e6:.0f} M")
        print(f"System CapEx:        {project.system_capex/1e6:.0f} M")
        print(f"Turbine CapEx:       {project.turbine_capex/1e6:.0f} M")
        print(f"Soft CapEx:          {project.soft_capex/1e6:.0f} M")
        print(f"Total CapEx:        {project.total_capex/1e6:.0f} M")
        print(f"Annual OpEx Rate:        {max(project.monthly_opex.values())*12:.0f} ")
        print(f"\nInstallation Time: {project.installation_time:.0f} h")
        print("\nN Substations: ", (project.phases["ElectricalDesign"].num_substations))
        print("N cables: ", (project.phases["ElectricalDesign"].num_cables))
        print("\n")

        # cable cost breakdown
        print("Cable specific costs")
        print(
            "Export cable installation CAPEX: %.2f M USD"
            % (project.phases["ExportCableInstallation"].installation_capex * 1e-6)
        )
        print("\n")

    return project, hybrid_substation_project


def adjust_orbit_costs(orbit_project, h2integrate_config):
    if ("expected_plant_cost" in h2integrate_config["finance_parameters"]["wind"]) and (
        h2integrate_config["finance_parameters"]["wind"]["expected_plant_cost"] != "none"
    ):
        wind_capex_multiplier = (
            h2integrate_config["finance_parameters"]["wind"]["expected_plant_cost"] * 1e9
        ) / orbit_project.total_capex
    else:
        wind_capex_multiplier = 1.0

    wind_total_capex = orbit_project.total_capex * wind_capex_multiplier
    wind_capex_breakdown = orbit_project.capex_breakdown
    for key in wind_capex_breakdown.keys():
        wind_capex_breakdown[key] *= wind_capex_multiplier

    return wind_total_capex, wind_capex_breakdown, wind_capex_multiplier


def breakout_export_costs_from_orbit_results(orbit_project, h2integrate_config, design_scenario):
    # adjust wind capex to meet expectations
    wind_total_capex, wind_capex_breakdown, wind_capex_multiplier = adjust_orbit_costs(
        orbit_project=orbit_project, h2integrate_config=h2integrate_config
    )

    # onshore substation cost not included in ORBIT costs by default, so add it separately
    total_wind_installed_costs_with_export = wind_total_capex

    # breakout export system costs
    array_cable_equipment_cost = wind_capex_breakdown["Array System"]
    array_cable_installation_cost = wind_capex_breakdown["Array System Installation"]
    total_array_cable_system_capex = array_cable_equipment_cost + array_cable_installation_cost

    export_cable_equipment_cost = wind_capex_breakdown[
        "Export System"
    ]  # this should include the onshore substation
    export_cable_installation_cost = wind_capex_breakdown["Export System Installation"]
    substation_equipment_cost = wind_capex_breakdown["Offshore Substation"]
    substation_installation_cost = wind_capex_breakdown["Offshore Substation Installation"]
    total_export_cable_system_capex = export_cable_equipment_cost + export_cable_installation_cost

    total_offshore_substation_capex = substation_equipment_cost + substation_installation_cost

    total_electrical_export_system_cost = (
        total_array_cable_system_capex
        + total_offshore_substation_capex
        + total_export_cable_system_capex
    )

    ## adjust wind cost to remove export
    if design_scenario["transportation"] == "hvdc+pipeline":
        unused_export_system_cost = 0.0
    elif (
        design_scenario["electrolyzer_location"] == "turbine"
        and design_scenario["h2_storage_location"] == "turbine"
    ):
        unused_export_system_cost = (
            total_array_cable_system_capex
            + total_export_cable_system_capex
            + total_offshore_substation_capex
        )
    elif (
        design_scenario["electrolyzer_location"] == "turbine"
        and design_scenario["h2_storage_location"] == "platform"
    ):
        unused_export_system_cost = total_export_cable_system_capex  # TODO check assumptions here
    elif (
        design_scenario["electrolyzer_location"] == "platform"
        and design_scenario["h2_storage_location"] == "platform"
    ):
        unused_export_system_cost = total_export_cable_system_capex  # TODO check assumptions here
    elif (
        design_scenario["electrolyzer_location"] == "platform"
        or design_scenario["electrolyzer_location"] == "turbine"
    ) and design_scenario["h2_storage_location"] == "onshore":
        unused_export_system_cost = total_export_cable_system_capex  # TODO check assumptions here
    else:
        unused_export_system_cost = 0.0

    total_used_export_system_costs = total_electrical_export_system_cost - unused_export_system_cost

    total_wind_cost_no_export = (
        total_wind_installed_costs_with_export - total_used_export_system_costs
    )

    return total_wind_cost_no_export, total_used_export_system_costs


def run_capex(
    hopp_results,
    wind_cost_results,
    electrolyzer_cost_results,
    h2_pipe_array_results,
    h2_transport_compressor_results,
    h2_transport_pipe_results,
    h2_storage_results,
    hopp_config,
    h2integrate_config,
    design_scenario,
    desal_results,
    platform_results,
    verbose=False,
):
    # total_wind_cost_no_export, total_used_export_system_costs = breakout_export_costs_from_orbit_results(orbit_project, h2integrate_config, design_scenario)  # noqa: E501

    # if orbit_hybrid_electrical_export_project is not None:
    #     _, total_used_export_system_costs = breakout_export_costs_from_orbit_results(orbit_hybrid_electrical_export_project, h2integrate_config, design_scenario)  # noqa: E501

    # wave capex
    if hopp_config["site"]["wave"]:
        cost_dict = hopp_results["hybrid_plant"].wave.mhk_costs.cost_outputs

        wcapex = (
            cost_dict["structural_assembly_cost_modeled"]
            + cost_dict["power_takeoff_system_cost_modeled"]
            + cost_dict["mooring_found_substruc_cost_modeled"]
        )
        wbos = (
            cost_dict["development_cost_modeled"]
            + cost_dict["eng_and_mgmt_cost_modeled"]
            + cost_dict["plant_commissioning_cost_modeled"]
            + cost_dict["site_access_port_staging_cost_modeled"]
            + cost_dict["assembly_and_install_cost_modeled"]
            + cost_dict["other_infrastructure_cost_modeled"]
        )
        welec_infrastruc_costs = (
            cost_dict["array_cable_system_cost_modeled"]
            + cost_dict["export_cable_system_cost_modeled"]
            + cost_dict["other_elec_infra_cost_modeled"]
        )  # +\
        # cost_dict['onshore_substation_cost_modeled']+\
        # cost_dict['offshore_substation_cost_modeled']
        # financial = cost_dict['project_contingency']+\
        # cost_dict['insurance_during_construction']+\
        # cost_dict['reserve_accounts']
        wave_capex = wcapex + wbos + welec_infrastruc_costs
    else:
        wave_capex = 0.0

    # solar capex
    if "pv" in hopp_config["technologies"].keys():
        solar_capex = hopp_results["hybrid_plant"].pv.total_installed_cost
    else:
        solar_capex = 0.0

    # battery capex
    if "battery" in hopp_config["technologies"].keys():
        battery_capex = hopp_results["hybrid_plant"].battery.total_installed_cost
    else:
        battery_capex = 0.0

    # TODO bos capex
    # bos_capex = hopp_results["hybrid_plant"].bos.total_installed_cost

    ## desal capex
    if desal_results is not None:
        desal_capex = desal_results["desal_capex_usd"]
    else:
        desal_capex = 0.0

    ## electrolyzer capex
    electrolyzer_total_capital_cost = electrolyzer_cost_results["electrolyzer_total_capital_cost"]

    if (
        design_scenario["electrolyzer_location"] == "platform"
        or design_scenario["h2_storage_location"] == "platform"
        or hopp_config["site"]["solar"]
    ):
        platform_costs = platform_results["capex"]
    else:
        platform_costs = 0.0

    # h2 transport
    h2_transport_compressor_capex = h2_transport_compressor_results["compressor_capex"]
    h2_transport_pipe_capex = h2_transport_pipe_results["total capital cost [$]"][0]

    ## h2 storage
    if h2integrate_config["h2_storage"]["type"] == "none":
        h2_storage_capex = 0.0
    elif (
        h2integrate_config["h2_storage"]["type"] == "pipe"
    ):  # ug pipe storage model includes compression
        h2_storage_capex = h2_storage_results["storage_capex"]
    elif (
        h2integrate_config["h2_storage"]["type"] == "turbine"
    ):  # ug pipe storage model includes compression
        h2_storage_capex = h2_storage_results["storage_capex"]
    elif (
        h2integrate_config["h2_storage"]["type"] == "pressure_vessel"
    ):  # pressure vessel storage model includes compression
        h2_storage_capex = h2_storage_results["storage_capex"]
    elif (
        h2integrate_config["h2_storage"]["type"] == "salt_cavern"
    ):  # salt cavern storage model includes compression
        h2_storage_capex = h2_storage_results["storage_capex"]
    elif (
        h2integrate_config["h2_storage"]["type"] == "lined_rock_cavern"
    ):  # lined rock cavern storage model includes compression
        h2_storage_capex = h2_storage_results["storage_capex"]
    else:
        msg = (
            f'the storage type you have indicated ({h2integrate_config["h2_storage"]["type"]}) '
            'has not been implemented.'
        )
        raise NotImplementedError(msg)

    # store capex component breakdown
    capex_breakdown = {
        "wind": wind_cost_results.total_wind_cost_no_export,
        "wave": wave_capex,
        "solar": solar_capex,
        "battery": battery_capex,
        "platform": platform_costs,
        "electrical_export_system": wind_cost_results.total_used_export_system_costs,
        "desal": desal_capex,
        "electrolyzer": electrolyzer_total_capital_cost,
        "h2_pipe_array": h2_pipe_array_results["capex"],
        "h2_transport_compressor": h2_transport_compressor_capex,
        "h2_transport_pipeline": h2_transport_pipe_capex,
        "h2_storage": h2_storage_capex,
    }

    # discount capex to appropriate year for unified costing
    for key in capex_breakdown.keys():
        if key == "h2_storage":
            # if design_scenario["h2_storage_location"] == "turbine" and h2integrate_config["h2_storage"]["type"] == "turbine":  # noqa: E501
            #     cost_year = h2integrate_config["finance_parameters"]["discount_years"][key][
            #         design_scenario["h2_storage_location"]
            #     ]
            # else:
            cost_year = h2integrate_config["finance_parameters"]["discount_years"][key][
                h2integrate_config["h2_storage"]["type"]
            ]
        else:
            cost_year = h2integrate_config["finance_parameters"]["discount_years"][key]

        capex_breakdown[key] = adjust_dollar_year(
            capex_breakdown[key],
            cost_year,
            h2integrate_config["project_parameters"]["cost_year"],
            h2integrate_config["finance_parameters"]["costing_general_inflation"],
        )

    total_system_installed_cost = sum(capex_breakdown[key] for key in capex_breakdown.keys())

    if verbose:
        print("\nCAPEX Breakdown")
        for key in capex_breakdown.keys():
            print(key, "%.2f" % (capex_breakdown[key] * 1e-6), " M")

        print(
            "\nTotal system CAPEX: ",
            "$%.2f" % (total_system_installed_cost * 1e-9),
            " B",
        )

    return total_system_installed_cost, capex_breakdown


def run_fixed_opex(
    hopp_results,
    wind_cost_results,
    electrolyzer_cost_results,
    h2_pipe_array_results,
    h2_transport_compressor_results,
    h2_transport_pipe_results,
    h2_storage_results,
    hopp_config,
    h2integrate_config,
    desal_results,
    platform_results,
    verbose=False,
    total_export_system_cost=0,
):
    # WIND ONLY Total O&M expenses including fixed, variable, and capacity-based, $/year
    # use values from hybrid substation if a hybrid plant
    # if orbit_hybrid_electrical_export_project is None:

    # wave opex
    if hopp_config["site"]["wave"]:
        cost_dict = hopp_results["hybrid_plant"].wave.mhk_costs.cost_outputs
        wave_opex = cost_dict["maintenance_cost"] + cost_dict["operations_cost"]
    else:
        wave_opex = 0.0

    # solar opex
    if "pv" in hopp_config["technologies"].keys():
        solar_opex = hopp_results["hybrid_plant"].pv.om_total_expense[0]
        if solar_opex < 0.1:
            raise (RuntimeWarning(f"Solar OPEX returned as {solar_opex}"))
    else:
        solar_opex = 0.0

    # battery opex
    if "battery" in hopp_config["technologies"].keys():
        battery_opex = hopp_results["hybrid_plant"].battery.om_total_expense[0]
        if battery_opex < 0.1:
            raise (RuntimeWarning(f"Battery OPEX returned as {battery_opex}"))
    else:
        battery_opex = 0.0

    # H2 OPEX
    platform_operating_costs = platform_results["opex"]  # TODO update this

    annual_operating_cost_h2 = electrolyzer_cost_results["electrolyzer_OM_cost_annual"]

    h2_transport_compressor_opex = h2_transport_compressor_results["compressor_opex"]  # annual

    h2_transport_pipeline_opex = h2_transport_pipe_results["annual operating cost [$]"][0]  # annual

    storage_opex = h2_storage_results["storage_opex"]
    # desal OPEX
    if desal_results is not None:
        desal_opex = desal_results["desal_opex_usd_per_year"]
    else:
        desal_opex = 0.0
    annual_operating_cost_desal = desal_opex

    # store opex component breakdown
    opex_breakdown_annual = {
        "wind_and_electrical": wind_cost_results.annual_operating_cost_wind,
        "platform": platform_operating_costs,
        #   "electrical_export_system": total_export_om_cost,
        "wave": wave_opex,
        "solar": solar_opex,
        "battery": battery_opex,
        "desal": annual_operating_cost_desal,
        "electrolyzer": annual_operating_cost_h2,
        "h2_pipe_array": h2_pipe_array_results["opex"],
        "h2_transport_compressor": h2_transport_compressor_opex,
        "h2_transport_pipeline": h2_transport_pipeline_opex,
        "h2_storage": storage_opex,
    }

    # discount opex to appropriate year for unified costing
    for key in opex_breakdown_annual.keys():
        if key == "h2_storage":
            cost_year = h2integrate_config["finance_parameters"]["discount_years"][key][
                h2integrate_config["h2_storage"]["type"]
            ]
        else:
            cost_year = h2integrate_config["finance_parameters"]["discount_years"][key]

        opex_breakdown_annual[key] = adjust_dollar_year(
            opex_breakdown_annual[key],
            cost_year,
            h2integrate_config["project_parameters"]["cost_year"],
            h2integrate_config["finance_parameters"]["costing_general_inflation"],
        )

    # Calculate the total annual OPEX of the installed system
    total_annual_operating_costs = sum(opex_breakdown_annual.values())

    if verbose:
        print("\nAnnual OPEX Breakdown")
        for key in opex_breakdown_annual.keys():
            print(key, "%.2f" % (opex_breakdown_annual[key] * 1e-6), " M")

        print(
            "\nTotal Annual OPEX: ",
            "$%.2f" % (total_annual_operating_costs * 1e-6),
            " M",
        )
        print(opex_breakdown_annual)
    return total_annual_operating_costs, opex_breakdown_annual


def run_variable_opex(
    electrolyzer_cost_results,
    h2integrate_config,
):
    """calculate variable O&M in $/kg-H2.

    Args:
        electrolyzer_cost_results (dict): output of
            h2integrate.tools.eco.electrolysis.run_electrolyzer_cost
        h2integrate_config (:obj:`h2integrate_simulation.H2IntegrateSimulationConfig`): H2Integrate
            simulation config.

    Returns:
        dict: dictionary of components and corresponding variable O&M in $/kg-H2 for
            adjusted for inflation so cost is in dollar-year corresponding to
            `h2integrate_config["project_parameters"]["cost_year"]`
    """
    electrolyzer_vom = electrolyzer_cost_results["electrolyzer_variable_OM_annual"]

    vopex_breakdown_annual = {"electrolyzer": electrolyzer_vom}

    for key in vopex_breakdown_annual.keys():
        cost_year = h2integrate_config["finance_parameters"]["discount_years"][key]
        vopex_breakdown_annual[key] = adjust_dollar_year(
            vopex_breakdown_annual[key],
            cost_year,
            h2integrate_config["project_parameters"]["cost_year"],
            h2integrate_config["finance_parameters"]["costing_general_inflation"],
        )
    return vopex_breakdown_annual


def calc_financial_parameter_weighted_average_by_capex(
    parameter_name: str, h2integrate_config: dict, capex_breakdown: dict
) -> float:
    """Allows the user to provide individual financial parameters for each technology in the system.
        The values given will be weighted by their CAPEX values to determine the final
        weighted-average parameter value to be supplied to the financial model. If only one
        technology has a unique parameter value, a "general" parameter value in the dictionary and
        that will be used for all technologies not specified individually.

    Args:
        parameter_name (str): The name of the parameter to be weighted by capex. The name should
            correspond to the name in the h2integrate config
        h2integrate_config (dict): Dictionary form of the h2integrate config
        capex_breakdown (dict): Output from `run_capex`, a dictionary of all capital items for
            the financial model

    Returns:
        parameter_value (float): if the parameter in the h2integrate config is given as a
            dictionary, then the weighted average by capex parameter value is returnd. Otherwise no
            averaging is done and the value of the parameter in the h2integrate_config is returned.
    """

    if type(h2integrate_config["finance_parameters"][parameter_name]) is not dict:
        # if only one value is given for the parameter, use that value
        parameter_value = h2integrate_config["finance_parameters"][parameter_name]

    else:
        # assign capex amounts as weights
        weights = np.array(list(capex_breakdown.values()))

        # initialize value array
        values = np.zeros_like(weights)

        # assign values
        for i, key in enumerate(capex_breakdown.keys()):
            if key in h2integrate_config["finance_parameters"][parameter_name].keys():
                values[i] = h2integrate_config["finance_parameters"][parameter_name][key]
            elif capex_breakdown[key] == 0.0:
                values[i] = 0.0
            else:
                values[i] = h2integrate_config["finance_parameters"][parameter_name]["general"]

        # calcuated weighted average parameter value
        parameter_value = np.average(values, weights=weights)
    return parameter_value


def run_profast_lcoe(
    h2integrate_config,
    wind_cost_results,
    capex_breakdown,
    opex_breakdown,
    hopp_results,
    incentive_option,
    design_scenario,
    verbose=False,
    show_plots=False,
    save_plots=False,
    output_dir="./output/",
):
    if isinstance(output_dir, str):
        output_dir = Path(output_dir).resolve()
    gen_inflation = h2integrate_config["finance_parameters"]["inflation_rate"]

    # initialize dictionary of weights for averaging financial parameters
    finance_param_weights = {}

    if (
        design_scenario["h2_storage_location"] == "onshore"
        or design_scenario["electrolyzer_location"] == "onshore"
    ):
        if "land_cost" in h2integrate_config["finance_parameters"]:
            land_cost = h2integrate_config["finance_parameters"]["land_cost"]
        else:
            land_cost = 1e6  # TODO should model this
    else:
        land_cost = 0.0

    pf = ProFAST.ProFAST()
    pf.set_params(
        "commodity",
        {
            "name": "electricity",
            "unit": "kWh",
            "initial price": 100,
            "escalation": gen_inflation,
        },
    )
    pf.set_params(
        "capacity",
        np.sum(hopp_results["combined_hybrid_power_production_hopp"]) / 365.0,
    )  # kWh/day
    pf.set_params("maintenance", {"value": 0, "escalation": gen_inflation})
    pf.set_params(
        "analysis start year",
        h2integrate_config["project_parameters"]["financial_analysis_start_year"],
    )
    pf.set_params("operating life", h2integrate_config["project_parameters"]["project_lifetime"])
    pf.set_params(
        "installation months", h2integrate_config["project_parameters"]["installation_time"]
    )
    pf.set_params(
        "installation cost",
        {
            "value": 0,
            "depr type": "Straight line",
            "depr period": 4,
            "depreciable": False,
        },
    )
    if land_cost > 0:
        pf.set_params("non depr assets", land_cost)
        pf.set_params(
            "end of proj sale non depr assets",
            land_cost
            * (1 + gen_inflation) ** h2integrate_config["project_parameters"]["project_lifetime"],
        )
    pf.set_params("demand rampup", 0)
    pf.set_params("long term utilization", 1)
    pf.set_params("credit card fees", 0)
    pf.set_params("sales tax", h2integrate_config["finance_parameters"]["sales_tax_rate"])
    pf.set_params("license and permit", {"value": 00, "escalation": gen_inflation})
    pf.set_params("rent", {"value": 0, "escalation": gen_inflation})
    pf.set_params(
        "property tax and insurance",
        h2integrate_config["finance_parameters"]["property_tax"]
        + h2integrate_config["finance_parameters"]["property_insurance"],
    )
    pf.set_params(
        "admin expense",
        h2integrate_config["finance_parameters"]["administrative_expense_percent_of_sales"],
    )
    pf.set_params(
        "total income tax rate",
        h2integrate_config["finance_parameters"]["total_income_tax_rate"],
    )
    pf.set_params(
        "capital gains tax rate",
        h2integrate_config["finance_parameters"]["capital_gains_tax_rate"],
    )
    pf.set_params("sell undepreciated cap", True)
    pf.set_params("tax losses monetized", True)
    pf.set_params("general inflation rate", gen_inflation)

    pf.set_params("debt type", h2integrate_config["finance_parameters"]["debt_type"])
    pf.set_params("loan period if used", h2integrate_config["finance_parameters"]["loan_period"])

    pf.set_params("cash onhand", h2integrate_config["finance_parameters"]["cash_onhand_months"])

    # ----------------------------------- Add capital items to ProFAST ----------------
    if "wind" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Wind system",
            cost=capex_breakdown["wind"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["wind"] = capex_breakdown["wind"]
    if "wave" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Wave system",
            cost=capex_breakdown["wave"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["wave"] = capex_breakdown["wave"]
    if "solar" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Solar PV system",
            cost=capex_breakdown["solar"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["solar"] = capex_breakdown["solar"]
    if "battery" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Battery system",
            cost=capex_breakdown["battery"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["battery"] = capex_breakdown["battery"]
    if design_scenario["transportation"] == "hvdc+pipeline" or not (
        design_scenario["electrolyzer_location"] == "turbine"
        and design_scenario["h2_storage_location"] == "turbine"
    ):
        pf.add_capital_item(
            name="Electrical export system",
            cost=capex_breakdown["electrical_export_system"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["electrical_export_system"] = capex_breakdown[
            "electrical_export_system"
        ]
    # -------------------------------------- Add fixed costs--------------------------------
    pf.add_fixed_cost(
        name="Wind and electrical fixed O&M cost",
        usage=1.0,
        unit="$/year",
        cost=opex_breakdown["wind_and_electrical"],
        escalation=gen_inflation,
    )

    if "wave" in opex_breakdown.keys():
        pf.add_fixed_cost(
            name="Wave O&M cost",
            usage=1.0,
            unit="$/year",
            cost=opex_breakdown["wave"],
            escalation=gen_inflation,
        )

    if "solar" in opex_breakdown.keys():
        pf.add_fixed_cost(
            name="Solar O&M cost",
            usage=1.0,
            unit="$/year",
            cost=opex_breakdown["solar"],
            escalation=gen_inflation,
        )

    if "battery" in opex_breakdown.keys():
        pf.add_fixed_cost(
            name="Battery O&M cost",
            usage=1.0,
            unit="$/year",
            cost=opex_breakdown["battery"],
            escalation=gen_inflation,
        )

    # ------------------------------------- add incentives -----------------------------------
    """
    Note: ptc units must be given to ProFAST in terms of dollars per unit of the primary commodity
    being produced

    Note: full tech-nutral (wind) tax credits are no longer available if constructions starts after
    Jan. 1 2034 (Jan 1. 2033 for h2 ptc)
    """

    # catch incentive option and add relevant incentives
    incentive_dict = h2integrate_config["policy_parameters"][f"option{incentive_option}"]
    # add electricity_ptc ($/kW)
    # adjust from 1992 dollars to start year
    wind_ptc_in_dollars_per_kw = -npf.fv(
        h2integrate_config["finance_parameters"]["costing_general_inflation"],
        h2integrate_config["project_parameters"]["financial_analysis_start_year"]
        + round(wind_cost_results.installation_time / 12)
        - 1992,
        0,
        incentive_dict["electricity_ptc"],
    )  # given in 1992 dollars but adjust for inflation

    pf.add_incentive(
        name="Electricity PTC",
        value=wind_ptc_in_dollars_per_kw,
        decay=-gen_inflation,
        sunset_years=10,
        tax_credit=True,
    )  # TODO check decay

    # ----------------------- Add weight-averaged parameters -----------------------

    equity_discount_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="discount_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )
    pf.set_params(
        "leverage after tax nominal discount rate",
        equity_discount_rate,
    )

    debt_interest_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="debt_interest_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )
    pf.set_params(
        "debt interest rate",
        debt_interest_rate,
    )

    if "debt_equity_split" in h2integrate_config["finance_parameters"].keys():
        debt_equity_split = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_split",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            (debt_equity_split / (100 - debt_equity_split)),
        )
    elif "debt_equity_ratio" in h2integrate_config["finance_parameters"].keys():
        debt_equity_ratio = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_ratio",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            debt_equity_ratio,
        )
    else:
        msg = (
            "missing value in `finance_parameters`. "
            "Requires either `debt_equity_ratio` or `debt_equity_split`"
        )
        raise ValueError(msg)

    # ---------------------- Run ProFAST -------------------------------------------
    sol = pf.solve_price()

    lcoe = sol["price"]

    if verbose:
        print("\nProFAST LCOE: ", "%.2f" % (lcoe * 1e3), "$/MWh")

    # -------------------------- Plots ---------------------------------------------
    if show_plots or save_plots:
        savepath = output_dir / "figures/wind_only"
        if not savepath.exists():
            savepath.mkdir(parents=True)
        pf.plot_costs_yearly(
            per_kg=False,
            scale="M",
            remove_zeros=True,
            remove_depreciation=False,
            fileout=savepath / f'annual_cash_flow_wind_only_{design_scenario["id"]}.png',
            show_plot=show_plots,
        )
        pf.plot_costs_yearly2(
            per_kg=False,
            scale="M",
            remove_zeros=True,
            remove_depreciation=False,
            fileout=savepath / f'annual_cash_flow_wind_only_{design_scenario["id"]}.html',
            show_plot=show_plots,
        )
        pf.plot_capital_expenses(
            fileout=savepath / f'capital_expense_only_{design_scenario["id"]}.png',
            show_plot=show_plots,
        )
        pf.plot_cashflow(
            fileout=savepath / f'cash_flow_wind_only_{design_scenario["id"]}.png',
            show_plot=show_plots,
        )
        pf.plot_costs(
            fileout=savepath / f'cost_breakdown_{design_scenario["id"]}.png',
            show_plot=show_plots,
        )

    return lcoe, pf, sol


def run_profast_grid_only(
    h2integrate_config,
    wind_cost_results,
    electrolyzer_performance_results,
    capex_breakdown,
    opex_breakdown_total,
    hopp_results,
    design_scenario,
    total_accessory_power_renewable_kw,
    total_accessory_power_grid_kw,
    verbose=False,
    show_plots=False,
    save_plots=False,
    output_dir="./output/",
):
    vopex_breakdown = opex_breakdown_total["variable_om"]
    fopex_breakdown = opex_breakdown_total["fixed_om"]

    if isinstance(output_dir, str):
        output_dir = Path(output_dir).resolve()
    gen_inflation = h2integrate_config["finance_parameters"]["inflation_rate"]

    # initialize dictionary of weights for averaging financial parameters
    finance_param_weights = {}

    if (
        design_scenario["h2_storage_location"] == "onshore"
        or design_scenario["electrolyzer_location"] == "onshore"
    ):
        if "land_cost" in h2integrate_config["finance_parameters"]:
            land_cost = h2integrate_config["finance_parameters"]["land_cost"]
        else:
            land_cost = 1e6  # TODO should model this
    else:
        land_cost = 0.0

    pf = ProFAST.ProFAST()
    pf.set_params(
        "commodity",
        {
            "name": "Hydrogen",
            "unit": "kg",
            "initial price": 100,
            "escalation": gen_inflation,
        },
    )
    pf.set_params(
        "capacity",
        electrolyzer_performance_results.rated_capacity_kg_pr_day,
    )  # kg/day
    pf.set_params("maintenance", {"value": 0, "escalation": gen_inflation})
    # TODO: update analysis start year below (ESG)
    pf.set_params(
        "analysis start year",
        h2integrate_config["project_parameters"]["financial_analysis_start_year"],
    )
    pf.set_params("operating life", h2integrate_config["project_parameters"]["project_lifetime"])
    pf.set_params(
        "installation cost",
        {
            "value": 0,
            "depr type": "Straight line",
            "depr period": 4,
            "depreciable": False,
        },
    )
    if land_cost > 0:
        pf.set_params("non depr assets", land_cost)
        pf.set_params(
            "end of proj sale non depr assets",
            land_cost
            * (1 + gen_inflation) ** h2integrate_config["project_parameters"]["project_lifetime"],
        )
    pf.set_params("demand rampup", 0)
    pf.set_params("long term utilization", electrolyzer_performance_results.long_term_utilization)
    pf.set_params("credit card fees", 0)
    pf.set_params("sales tax", h2integrate_config["finance_parameters"]["sales_tax_rate"])
    pf.set_params("license and permit", {"value": 00, "escalation": gen_inflation})
    pf.set_params("rent", {"value": 0, "escalation": gen_inflation})
    pf.set_params(
        "property tax and insurance",
        h2integrate_config["finance_parameters"]["property_tax"]
        + h2integrate_config["finance_parameters"]["property_insurance"],
    )
    pf.set_params(
        "admin expense",
        h2integrate_config["finance_parameters"]["administrative_expense_percent_of_sales"],
    )
    pf.set_params(
        "total income tax rate",
        h2integrate_config["finance_parameters"]["total_income_tax_rate"],
    )
    pf.set_params(
        "capital gains tax rate",
        h2integrate_config["finance_parameters"]["capital_gains_tax_rate"],
    )
    pf.set_params("sell undepreciated cap", True)
    pf.set_params("tax losses monetized", True)
    pf.set_params("general inflation rate", gen_inflation)

    pf.set_params("debt type", h2integrate_config["finance_parameters"]["debt_type"])
    pf.set_params("loan period if used", h2integrate_config["finance_parameters"]["loan_period"])

    pf.set_params("cash onhand", h2integrate_config["finance_parameters"]["cash_onhand_months"])

    # ----------------------------------- Add capital items to ProFAST ----------------

    pf.add_capital_item(
        name="Electrolysis system",
        cost=capex_breakdown["electrolyzer"],
        depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
        depr_period=h2integrate_config["finance_parameters"]["depreciation_period_electrolyzer"],
        refurb=electrolyzer_performance_results.refurb_cost_percent,
    )
    finance_param_weights["electrolyzer"] = capex_breakdown["electrolyzer"]
    pf.add_capital_item(
        name="Hydrogen storage system",
        cost=capex_breakdown["h2_storage"],
        depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
        depr_period=h2integrate_config["finance_parameters"]["depreciation_period_electrolyzer"],
        refurb=[0],
    )
    finance_param_weights["h2_storage"] = capex_breakdown["h2_storage"]
    # -------------------------------------- Add fixed costs--------------------------------
    pf.add_fixed_cost(
        name="Electrolyzer fixed O&M cost",
        usage=1.0,
        unit="$/year",
        cost=fopex_breakdown["electrolyzer"],
        escalation=gen_inflation,
    )
    pf.add_fixed_cost(
        name="Hydrogen storage fixed O&M cost",
        usage=1.0,
        unit="$/year",
        cost=fopex_breakdown["h2_storage"],
        escalation=gen_inflation,
    )

    # ---------------------- Add feedstocks, note the various cost options-------------------
    pf.add_feedstock(
        name="Water",
        usage=electrolyzer_performance_results.water_usage_gal_pr_kg,
        unit="gal",
        cost="US Average",
        escalation=gen_inflation,
    )
    pf.add_feedstock(
        name="Electrolyzer Variable O&M",
        usage=1.0,
        unit="$/kg",
        cost=vopex_breakdown["electrolyzer"],
        escalation=gen_inflation,
    )

    # if h2integrate_config["project_parameters"]["grid_connection"]:

    energy_purchase = (
        365 * 24 * h2integrate_config["electrolyzer"]["rating"] * 1e3
        + sum(total_accessory_power_renewable_kw)
        + sum(total_accessory_power_grid_kw)
    )

    pf.add_fixed_cost(
        name="Electricity from grid",
        usage=1.0,
        unit="$/year",
        cost=energy_purchase * h2integrate_config["project_parameters"]["ppa_price"],
        escalation=gen_inflation,
    )

    # ----------------------- Add weight-averaged parameters -----------------------

    equity_discount_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="discount_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )

    pf.set_params(
        "leverage after tax nominal discount rate",
        equity_discount_rate,
    )

    debt_interest_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="debt_interest_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )
    pf.set_params(
        "debt interest rate",
        debt_interest_rate,
    )

    if "debt_equity_split" in h2integrate_config["finance_parameters"].keys():
        debt_equity_split = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_split",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            (debt_equity_split / (100 - debt_equity_split)),
        )
    elif "debt_equity_ratio" in h2integrate_config["finance_parameters"].keys():
        debt_equity_ratio = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_ratio",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            debt_equity_ratio,
        )
    else:
        msg = (
            "missing value in `finance_parameters`. "
            "Requires either `debt_equity_ratio` or `debt_equity_split`"
        )
        raise ValueError(msg)

    # ----------------------- Run ProFAST -----------------------------------------

    sol = pf.solve_price()

    lcoh = sol["price"]
    if verbose:
        print(f"\nLCOH grid only: {lcoh:.2f} $/kg")
        print(f'ProFAST grid only NPV: {sol["NPV"]:.2f}')
        print(f'ProFAST grid only IRR: {max(sol["irr"]):.5f}')
        print(f'ProFAST grid only LCO: {sol["lco"]:.2f} $/kg')
        print(f'ProFAST grid only Profit Index: {sol["profit index"]:.2f}')
        print(f'ProFAST grid only payback period: {sol["investor payback period"]}')

    # ----------------------- Plots -----------------------------------------------
    if save_plots or show_plots:
        savepaths = [
            output_dir / "figures/capex",
            output_dir / "figures/annual_cash_flow",
            output_dir / "figures/lcoh_breakdown",
            output_dir / "data",
        ]
        for savepath in savepaths:
            if not savepath.exists():
                savepath.mkdir(parents=True)

        pf.plot_capital_expenses(
            fileout=savepaths[0] / f"capital_expense_grid_only_{design_scenario['id']}.pdf",
            show_plot=show_plots,
        )
        pf.plot_cashflow(
            fileout=savepaths[1] / f"cash_flow_grid_only_{design_scenario['id']}.png",
            show_plot=show_plots,
        )

        pd.DataFrame.from_dict(data=pf.cash_flow_out, orient="index").to_csv(
            savepaths[3] / f"cash_flow_grid_only_{design_scenario['id']}.csv"
        )

        pf.plot_costs(
            savepaths[2] / f"lcoh_grid_only_{design_scenario['id']}",
            show_plot=show_plots,
        )
    return lcoh, pf, sol


def run_profast_full_plant_model(
    h2integrate_config,
    wind_cost_results,
    electrolyzer_performance_results,
    capex_breakdown,
    opex_breakdown_total,
    hopp_results,
    incentive_option,
    design_scenario,
    total_accessory_power_renewable_kw,
    total_accessory_power_grid_kw,
    verbose=False,
    show_plots=False,
    save_plots=False,
    output_dir="./output/",
):
    vopex_breakdown = opex_breakdown_total["variable_om"]
    fopex_breakdown = opex_breakdown_total["fixed_om"]

    if isinstance(output_dir, str):
        output_dir = Path(output_dir).resolve()
    gen_inflation = h2integrate_config["finance_parameters"]["inflation_rate"]

    if "financial_analysis_start_year" not in h2integrate_config["finance_parameters"]:
        financial_analysis_start_year = h2integrate_config["project_parameters"][
            "financial_analysis_start_year"
        ]
    else:
        financial_analysis_start_year = h2integrate_config["finance_parameters"][
            "financial_analysis_start_year"
        ]

    if "installation_time" not in h2integrate_config["project_parameters"]:
        installation_period_months = wind_cost_results.installation_time
    else:
        installation_period_months = h2integrate_config["project_parameters"]["installation_time"]

    # initialize dictionary of weights for averaging financial parameters
    finance_param_weights = {}

    if (
        design_scenario["h2_storage_location"] == "onshore"
        or design_scenario["electrolyzer_location"] == "onshore"
    ):
        if "land_cost" in h2integrate_config["finance_parameters"]:
            land_cost = h2integrate_config["finance_parameters"]["land_cost"]
        else:
            land_cost = 1e6  # TODO should model this
    else:
        land_cost = 0.0

    pf = ProFAST.ProFAST()
    pf.set_params(
        "commodity",
        {
            "name": "Hydrogen",
            "unit": "kg",
            "initial price": 100,
            "escalation": gen_inflation,
        },
    )
    pf.set_params(
        "capacity",
        electrolyzer_performance_results.rated_capacity_kg_pr_day,
    )  # kg/day
    pf.set_params("maintenance", {"value": 0, "escalation": gen_inflation})
    pf.set_params(
        "analysis start year",
        financial_analysis_start_year,
    )
    pf.set_params("operating life", h2integrate_config["project_parameters"]["project_lifetime"])
    pf.set_params(
        "installation months",
        installation_period_months,
    )
    pf.set_params(
        "installation cost",
        {
            "value": 0,
            "depr type": "Straight line",
            "depr period": 4,
            "depreciable": False,
        },
    )
    if land_cost > 0:
        pf.set_params("non depr assets", land_cost)
        pf.set_params(
            "end of proj sale non depr assets",
            land_cost
            * (1 + gen_inflation) ** h2integrate_config["project_parameters"]["project_lifetime"],
        )
    pf.set_params("demand rampup", 0)
    pf.set_params("long term utilization", electrolyzer_performance_results.long_term_utilization)
    pf.set_params("credit card fees", 0)
    pf.set_params("sales tax", h2integrate_config["finance_parameters"]["sales_tax_rate"])
    pf.set_params("license and permit", {"value": 00, "escalation": gen_inflation})
    pf.set_params("rent", {"value": 0, "escalation": gen_inflation})
    # TODO how to handle property tax and insurance for fully offshore?
    pf.set_params(
        "property tax and insurance",
        h2integrate_config["finance_parameters"]["property_tax"]
        + h2integrate_config["finance_parameters"]["property_insurance"],
    )
    pf.set_params(
        "admin expense",
        h2integrate_config["finance_parameters"]["administrative_expense_percent_of_sales"],
    )
    pf.set_params(
        "total income tax rate",
        h2integrate_config["finance_parameters"]["total_income_tax_rate"],
    )
    pf.set_params(
        "capital gains tax rate",
        h2integrate_config["finance_parameters"]["capital_gains_tax_rate"],
    )
    pf.set_params("sell undepreciated cap", True)
    pf.set_params("tax losses monetized", True)
    pf.set_params("general inflation rate", gen_inflation)

    pf.set_params("debt type", h2integrate_config["finance_parameters"]["debt_type"])
    pf.set_params("loan period if used", h2integrate_config["finance_parameters"]["loan_period"])
    pf.set_params("cash onhand", h2integrate_config["finance_parameters"]["cash_onhand_months"])

    # ----------------------------------- Add capital and fixed items to ProFAST ----------------
    if "wind" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Wind system",
            cost=capex_breakdown["wind"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["wind"] = capex_breakdown["wind"]

    if "wave" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Wave system",
            cost=capex_breakdown["wave"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["wave"] = capex_breakdown["wave"]

    if "solar" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Solar PV system",
            cost=capex_breakdown["solar"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["solar"] = capex_breakdown["solar"]

    if "battery" in capex_breakdown.keys():
        pf.add_capital_item(
            name="Battery system",
            cost=capex_breakdown["battery"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["battery"] = capex_breakdown["battery"]

    if "platform" in capex_breakdown.keys() and capex_breakdown["platform"] > 0:
        pf.add_capital_item(
            name="Equipment platform",
            cost=capex_breakdown["platform"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["platform"] = capex_breakdown["platform"]

        pf.add_fixed_cost(
            name="Equipment platform O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["platform"],
            escalation=gen_inflation,
        )

    pf.add_fixed_cost(
        name="Wind and electrical export fixed O&M cost",
        usage=1.0,
        unit="$/year",
        cost=fopex_breakdown["wind_and_electrical"],
        escalation=gen_inflation,
    )
    if "wave" in fopex_breakdown.keys():
        pf.add_fixed_cost(
            name="Wave O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["wave"],
            escalation=gen_inflation,
        )

    if "solar" in fopex_breakdown.keys():
        pf.add_fixed_cost(
            name="Solar O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["solar"],
            escalation=gen_inflation,
        )

    if "battery" in fopex_breakdown.keys():
        pf.add_fixed_cost(
            name="Battery O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["battery"],
            escalation=gen_inflation,
        )

    if design_scenario["transportation"] == "hvdc+pipeline" or not (
        design_scenario["electrolyzer_location"] == "turbine"
        and design_scenario["h2_storage_location"] == "turbine"
    ):
        pf.add_capital_item(
            name="Electrical export system",
            cost=capex_breakdown["electrical_export_system"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"]["depreciation_period"],
            refurb=[0],
        )
        finance_param_weights["electrical_export_system"] = capex_breakdown[
            "electrical_export_system"
        ]
        # TODO assess if this makes sense (electrical export O&M included in wind O&M)

    pf.add_capital_item(
        name="Electrolysis system",
        cost=capex_breakdown["electrolyzer"],
        depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
        depr_period=h2integrate_config["finance_parameters"]["depreciation_period_electrolyzer"],
        refurb=electrolyzer_performance_results.refurb_cost_percent,
    )
    finance_param_weights["electrolyzer"] = capex_breakdown["electrolyzer"]
    pf.add_fixed_cost(
        name="Electrolysis system fixed O&M cost",
        usage=1.0,
        unit="$/year",
        cost=fopex_breakdown["electrolyzer"],
        escalation=gen_inflation,
    )

    pf.add_feedstock(
        name="Electrolyzer Variable O&M",
        usage=1.0,
        unit="$/kg",
        cost=vopex_breakdown["electrolyzer"],
        escalation=gen_inflation,
    )

    if design_scenario["electrolyzer_location"] == "turbine":
        pf.add_capital_item(
            name="H2 pipe array system",
            cost=capex_breakdown["h2_pipe_array"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"][
                "depreciation_period_electrolyzer"
            ],
            refurb=[0],
        )
        finance_param_weights["h2_pipe_array"] = capex_breakdown["h2_pipe_array"]
        pf.add_fixed_cost(
            name="H2 pipe array fixed O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["h2_pipe_array"],
            escalation=gen_inflation,
        )

    if (
        (
            design_scenario["h2_storage_location"] == "onshore"
            and design_scenario["electrolyzer_location"] != "onshore"
        )
        or (
            design_scenario["h2_storage_location"] != "onshore"
            and design_scenario["electrolyzer_location"] == "onshore"
        )
        or (design_scenario["transportation"] == "hvdc+pipeline")
    ):
        pf.add_capital_item(
            name="H2 transport compressor system",
            cost=capex_breakdown["h2_transport_compressor"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"][
                "depreciation_period_electrolyzer"
            ],
            refurb=[0],
        )
        finance_param_weights["h2_transport_compressor"] = capex_breakdown[
            "h2_transport_compressor"
        ]
        pf.add_capital_item(
            name="H2 transport pipeline system",
            cost=capex_breakdown["h2_transport_pipeline"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"][
                "depreciation_period_electrolyzer"
            ],
            refurb=[0],
        )
        finance_param_weights["h2_transport_pipeline"] = capex_breakdown["h2_transport_pipeline"]

        pf.add_fixed_cost(
            name="H2 transport compression fixed O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["h2_transport_compressor"],
            escalation=gen_inflation,
        )
        pf.add_fixed_cost(
            name="H2 transport pipeline fixed O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["h2_transport_pipeline"],
            escalation=gen_inflation,
        )

    if h2integrate_config["h2_storage"]["type"] != "none":
        pf.add_capital_item(
            name="Hydrogen storage system",
            cost=capex_breakdown["h2_storage"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"][
                "depreciation_period_electrolyzer"
            ],
            refurb=[0],
        )
        finance_param_weights["h2_storage"] = capex_breakdown["h2_storage"]
        pf.add_fixed_cost(
            name="Hydrogen storage fixed O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["h2_storage"],
            escalation=gen_inflation,
        )

    # ---------------------- Add feedstocks, note the various cost options-------------------
    if design_scenario["electrolyzer_location"] == "onshore":
        pf.add_feedstock(
            name="Water",
            usage=electrolyzer_performance_results.water_usage_gal_pr_kg,
            unit="gal",
            cost="US Average",
            escalation=gen_inflation,
        )
    else:
        pf.add_capital_item(
            name="Desal system",
            cost=capex_breakdown["desal"],
            depr_type=h2integrate_config["finance_parameters"]["depreciation_method"],
            depr_period=h2integrate_config["finance_parameters"][
                "depreciation_period_electrolyzer"
            ],
            refurb=[0],
        )
        finance_param_weights["desal"] = capex_breakdown["desal"]
        pf.add_fixed_cost(
            name="Desal fixed O&M cost",
            usage=1.0,
            unit="$/year",
            cost=fopex_breakdown["desal"],
            escalation=gen_inflation,
        )

    if (
        h2integrate_config["project_parameters"]["grid_connection"]
        or sum(total_accessory_power_grid_kw) > 0
    ):
        energy_purchase = sum(total_accessory_power_grid_kw)  # * 365 * 24

        if h2integrate_config["project_parameters"]["grid_connection"]:
            annual_energy_shortfall = np.sum(hopp_results["energy_shortfall_hopp"])
            energy_purchase += annual_energy_shortfall

        pf.add_fixed_cost(
            name="Electricity from grid",
            usage=1.0,
            unit="$/year",
            cost=energy_purchase * h2integrate_config["project_parameters"]["ppa_price"],
            escalation=gen_inflation,
        )

    # ------------------------------------- add incentives -----------------------------------
    """
    Note: units must be given to ProFAST in terms of dollars per unit of the primary commodity being
    produced

    Note: full tech-nutral (wind) tax credits are no longer available if constructions starts after
    Jan. 1 2034 (Jan 1. 2033 for h2 ptc)
    """

    # catch incentive option and add relevant incentives
    incentive_dict = h2integrate_config["policy_parameters"][f"option{incentive_option}"]

    # add wind_itc (% of wind capex)
    electricity_itc_value_percent_wind_capex = incentive_dict["electricity_itc"]
    electricity_itc_value_dollars = electricity_itc_value_percent_wind_capex * (
        capex_breakdown["wind"] + capex_breakdown["electrical_export_system"]
    )
    pf.set_params(
        "one time cap inct",
        {
            "value": electricity_itc_value_dollars,
            "depr type": h2integrate_config["finance_parameters"]["depreciation_method"],
            "depr period": h2integrate_config["finance_parameters"]["depreciation_period"],
            "depreciable": True,
        },
    )

    # add h2_storage_itc (% of h2 storage capex)
    itc_value_percent_h2_store_capex = incentive_dict["h2_storage_itc"]
    electricity_itc_value_dollars_h2_store = (
        itc_value_percent_h2_store_capex * (capex_breakdown["h2_storage"])
    )
    pf.set_params(
        "one time cap inct",
        {
            "value": electricity_itc_value_dollars_h2_store,
            "depr type": h2integrate_config["finance_parameters"]["depreciation_method"],
            "depr period": h2integrate_config["finance_parameters"]["depreciation_period"],
            "depreciable": True,
        },
    )

    # add electricity_ptc ($/kW)
    # adjust from 1992 dollars to start year
    electricity_ptc_in_dollars_per_kw = -npf.fv(
        h2integrate_config["finance_parameters"]["costing_general_inflation"],
        h2integrate_config["project_parameters"]["financial_analysis_start_year"]
        + round(wind_cost_results.installation_time / 12)
        - 1992,
        0,
        incentive_dict["electricity_ptc"],
    )  # given in 1992 dollars but adjust for inflation
    kw_per_kg_h2 = sum(hopp_results["combined_hybrid_power_production_hopp"]) / np.mean(
        electrolyzer_performance_results.electrolyzer_annual_h2_production_kg
    )
    electricity_ptc_in_dollars_per_kg_h2 = electricity_ptc_in_dollars_per_kw * kw_per_kg_h2
    pf.add_incentive(
        name="Electricity PTC",
        value=electricity_ptc_in_dollars_per_kg_h2,
        decay=-gen_inflation,
        sunset_years=10,
        tax_credit=True,
    )  # TODO check decay

    # add h2_ptc ($/kg)
    h2_ptc_inflation_adjusted = -npf.fv(
        h2integrate_config["finance_parameters"][
            "costing_general_inflation"
        ],  # use ATB year (cost inflation 2.5%) costing_general_inflation
        h2integrate_config["project_parameters"]["financial_analysis_start_year"]
        + round(wind_cost_results.installation_time / 12)
        - 2022,
        0,
        incentive_dict["h2_ptc"],
    )
    pf.add_incentive(
        name="H2 PTC",
        value=h2_ptc_inflation_adjusted,
        decay=-gen_inflation,  # correct inflation
        sunset_years=10,
        tax_credit=True,
    )  # TODO check decay

    # ----------------------- Add weight-averaged parameters -----------------------

    equity_discount_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="discount_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )
    pf.set_params(
        "leverage after tax nominal discount rate",
        equity_discount_rate,
    )

    debt_interest_rate = calc_financial_parameter_weighted_average_by_capex(
        parameter_name="debt_interest_rate",
        h2integrate_config=h2integrate_config,
        capex_breakdown=finance_param_weights,
    )
    pf.set_params(
        "debt interest rate",
        debt_interest_rate,
    )

    if "debt_equity_split" in h2integrate_config["finance_parameters"].keys():
        debt_equity_split = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_split",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            (debt_equity_split / (100 - debt_equity_split)),
        )
    elif "debt_equity_ratio" in h2integrate_config["finance_parameters"].keys():
        debt_equity_ratio = calc_financial_parameter_weighted_average_by_capex(
            parameter_name="debt_equity_ratio",
            h2integrate_config=h2integrate_config,
            capex_breakdown=finance_param_weights,
        )
        pf.set_params(
            "debt equity ratio of initial financing",
            debt_equity_ratio,
        )
    else:
        msg = (
            "missing value in `finance_parameters`. "
            "Requires either `debt_equity_ratio` or `debt_equity_split`"
        )
        raise ValueError(msg)

    # ------------------------------------ solve and post-process -----------------------------

    sol = pf.solve_price()

    df = pf.cash_flow_out

    lcoh = sol["price"]

    if verbose:
        print(f"\nProFAST LCOH: {lcoh:.2f} $/kg")
        print(f'ProFAST NPV: {sol["NPV"]:.2f}')
        print(f'ProFAST IRR: {max(sol["irr"]):.5f}')
        print(f'ProFAST LCO: {sol["lco"]:.2f} $/kg')
        print(f'ProFAST Profit Index: {sol["profit index"]:.2f}')
        print(f'ProFAST payback period: {sol["investor payback period"]}')

        MIRR = npf.mirr(
            df["Investor cash flow"],
            debt_interest_rate,
            equity_discount_rate,
        )  # TODO probably ignore MIRR
        NPV = npf.npv(
            h2integrate_config["finance_parameters"]["inflation_rate"],
            df["Investor cash flow"],
        )
        ROI = np.sum(df["Investor cash flow"]) / abs(
            np.sum(df["Investor cash flow"][df["Investor cash flow"] < 0])
        )  # ROI is not a good way of thinking about the value of the project

        # TODO project level IRR - capex and operating cash flow

        # note: hurdle rate typically 20% IRR before investing in it due to typically optimistic
        # assumptions

        # note: negative retained earnings (keeping debt, paying down equity) - to get around it,
        # do another line for retained earnings and watch dividends paid by the project
        # (net income/equity should stay positive this way)

        print("Investor NPV: ", np.round(NPV * 1e-6, 2), "M USD")
        print("Investor MIRR: ", np.round(MIRR, 5), "")
        print("Investor ROI: ", np.round(ROI, 5), "")

    if save_plots or show_plots:
        savepaths = [
            output_dir / "figures/capex",
            output_dir / "figures/annual_cash_flow",
            output_dir / "figures/lcoh_breakdown",
            output_dir / "data",
        ]
        for savepath in savepaths:
            if not savepath.exists():
                savepath.mkdir(parents=True)

        pf.plot_capital_expenses(
            fileout=savepaths[0] / f"capital_expense_{design_scenario['id']}.pdf",
            show_plot=show_plots,
        )
        pf.plot_cashflow(
            fileout=savepaths[1] / f"cash_flow_{design_scenario['id']}.png",
            show_plot=show_plots,
        )

        pd.DataFrame.from_dict(data=pf.cash_flow_out).to_csv(
            savepaths[3] / f"cash_flow_{design_scenario['id']}.csv"
        )

        pf.plot_costs(
            savepaths[2] / f"lcoh_{design_scenario['id']}",
            show_plot=show_plots,
        )

    return lcoh, pf, sol
