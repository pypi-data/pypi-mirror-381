import os
import unittest
import importlib
from pathlib import Path

import numpy as np
import pytest
import openmdao.api as om

from h2integrate import EXAMPLE_DIR
from h2integrate.core.h2integrate_model import H2IntegrateModel


def test_steel_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "01_onshore_steel_mn")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "01_onshore_steel_mn.yaml")

    # Run the model
    model.run()

    model.post_process()
    # Subtests for checking specific values
    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.LCOH_delivered")[0], rel=1e-3
            )
            == 7.47944016
        )

    with subtests.test("Check LCOS"):
        assert pytest.approx(model.prob.get_val("steel.LCOS")[0], rel=1e-3) == 1213.87728644

    with subtests.test("Check total adjusted CapEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_capex_adjusted")[0], rel=1e-3
            )
            == 5.10869916e09
        )

    with subtests.test("Check total adjusted OpEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_opex_adjusted")[0], rel=1e-3
            )
            == 96349901.77625626
        )

    with subtests.test("Check steel CapEx"):
        assert pytest.approx(model.prob.get_val("steel.CapEx"), rel=1e-3) == 5.78060014e08

    with subtests.test("Check steel OpEx"):
        assert pytest.approx(model.prob.get_val("steel.OpEx"), rel=1e-3) == 1.0129052e08


def test_simple_ammonia_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "02_texas_ammonia")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "02_texas_ammonia.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check HOPP CapEx"):
        assert pytest.approx(model.prob.get_val("plant.hopp.hopp.CapEx"), rel=1e-3) == 1.75469962e09

    with subtests.test("Check HOPP OpEx"):
        assert pytest.approx(model.prob.get_val("plant.hopp.hopp.OpEx"), rel=1e-3) == 32953490.4

    with subtests.test("Check electrolyzer CapEx"):
        assert pytest.approx(model.prob.get_val("electrolyzer.CapEx"), rel=1e-3) == 6.00412524e08

    with subtests.test("Check electrolyzer OpEx"):
        assert pytest.approx(model.prob.get_val("electrolyzer.OpEx"), rel=1e-3) == 14703155.39207595

    with subtests.test("Check H2 storage CapEx"):
        assert (
            pytest.approx(model.prob.get_val("plant.h2_storage.h2_storage.CapEx"), rel=1e-3)
            == 65336874.189441
        )

    with subtests.test("Check H2 storage OpEx"):
        assert (
            pytest.approx(model.prob.get_val("plant.h2_storage.h2_storage.OpEx"), rel=1e-3)
            == 2358776.66234517
        )

    with subtests.test("Check ammonia CapEx"):
        assert pytest.approx(model.prob.get_val("ammonia.CapEx"), rel=1e-3) == 1.0124126e08

    with subtests.test("Check ammonia OpEx"):
        assert pytest.approx(model.prob.get_val("ammonia.OpEx"), rel=1e-3) == 11178036.31197754

    with subtests.test("Check total adjusted CapEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_capex_adjusted")[0], rel=1e-3
            )
            == 2577162708.3
        )

    with subtests.test("Check total adjusted OpEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_opex_adjusted")[0], rel=1e-3
            )
            == 53161706.5
        )

    # Currently underestimated compared to the Reference Design Doc
    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_hydrogen.LCOH")[0], rel=1e-3)
            == 3.970
        )
    # Currently underestimated compared to the Reference Design Doc
    with subtests.test("Check LCOA"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_ammonia.LCOA")[0], rel=1e-3)
            == 1.02470046
        )

    # Check that the expected output files exist
    outputs_dir = Path.cwd() / "outputs"
    assert (
        outputs_dir / "profast_output_ammonia_config.yaml"
    ).is_file(), "profast_output_ammonia.yaml not found"
    assert (
        outputs_dir / "profast_output_electricity_config.yaml"
    ).is_file(), "profast_output_electricity.yaml not found"
    assert (
        outputs_dir / "profast_output_hydrogen_config.yaml"
    ).is_file(), "profast_output_hydrogen.yaml not found"


def test_ammonia_synloop_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "12_ammonia_synloop")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "12_ammonia_synloop.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check HOPP CapEx"):
        assert pytest.approx(model.prob.get_val("plant.hopp.hopp.CapEx"), rel=1e-6) == 1.75469962e09

    with subtests.test("Check HOPP OpEx"):
        assert pytest.approx(model.prob.get_val("plant.hopp.hopp.OpEx"), rel=1e-6) == 32953490.4

    with subtests.test("Check electrolyzer CapEx"):
        assert pytest.approx(model.prob.get_val("electrolyzer.CapEx"), rel=1e-6) == 6.00412524e08

    with subtests.test("Check electrolyzer OpEx"):
        assert pytest.approx(model.prob.get_val("electrolyzer.OpEx"), rel=1e-6) == 14703155.39207595

    with subtests.test("Check H2 storage CapEx"):
        assert (
            pytest.approx(model.prob.get_val("plant.h2_storage.h2_storage.CapEx"), rel=1e-6)
            == 65337437.18075897
        )

    with subtests.test("Check H2 storage OpEx"):
        assert (
            pytest.approx(model.prob.get_val("plant.h2_storage.h2_storage.OpEx"), rel=1e-6)
            == 2358794.11507603
        )

    with subtests.test("Check ammonia CapEx"):
        assert pytest.approx(model.prob.get_val("ammonia.CapEx"), rel=1e-6) == 1.15173753e09

    with subtests.test("Check ammonia OpEx"):
        assert pytest.approx(model.prob.get_val("ammonia.OpEx"), rel=1e-6) == 25318447.90064406

    with subtests.test("Check total adjusted CapEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_nh3.total_capex_adjusted")[0], rel=1e-6
            )
            == 3.7289e09
        )

    with subtests.test("Check total adjusted OpEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_nh3.total_opex_adjusted")[0], rel=1e-6
            )
            == 78480154.4
        )

    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_h2.LCOH")[0], rel=1e-6)
            == 3.9705799098258776
        )

    with subtests.test("Check LCOA"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_nh3.LCOA")[0], rel=1e-6)
            == 1.067030996544544
        )


def test_smr_methanol_example(subtests):
    # Change the current working directory to the SMR example's directory
    os.chdir(EXAMPLE_DIR / "03_methanol" / "smr")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "03_smr_methanol.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Check levelized cost of methanol (LCOM)
    with subtests.test("Check SMR LCOM"):
        assert pytest.approx(model.prob.get_val("methanol.LCOM"), rel=1e-6) == 0.22116813


def test_co2h_methanol_example(subtests):
    # Change the current working directory to the CO2 Hydrogenation example's directory
    os.chdir(EXAMPLE_DIR / "03_methanol" / "co2_hydrogenation")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "03_co2h_methanol.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Check levelized cost of methanol (LCOM)
    with subtests.test("Check CO2 Hydrogenation LCOM"):
        assert pytest.approx(model.prob.get_val("methanol.LCOM")[0], rel=1e-6) == 1.381162


def test_wind_h2_opt_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "05_wind_h2_opt")

    # Run without optimization
    model_init = H2IntegrateModel(Path.cwd() / "wind_plant_electrolyzer0.yaml")

    # Run the model
    model_init.run()

    model_init.post_process()

    annual_h20 = model_init.prob.get_val("electrolyzer.total_hydrogen_produced", units="kg/year")[0]

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "wind_plant_electrolyzer.yaml")

    # Run the model
    model.run()

    with subtests.test("Check initial H2 production"):
        assert annual_h20 < (60500000 - 10000)

    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_electricity.LCOE")[0], rel=1e-3)
            == 0.059096
        )

    with subtests.test("Check electrolyzer size"):
        assert (
            pytest.approx(model.prob.get_val("electrolyzer.electrolyzer_size_mw")[0], rel=1e-3)
            == 1380.0
        )
    # Read the resulting SQL file and compare initial and final LCOH values

    sql_path = None
    for root, _dirs, files in os.walk(Path.cwd()):
        for file in files:
            if file == "wind_h2_opt.sql":
                sql_path = Path(root) / file
                break
        if sql_path:
            break
    assert (
        sql_path is not None
    ), "wind_h2_opt.sql file not found in current working directory or subdirectories."

    cr = om.CaseReader(str(sql_path))
    cases = list(cr.get_cases())
    assert len(cases) > 1, "Not enough cases recorded in SQL file."

    # Get initial and final LCOH values
    initial_lcoh = cases[0].outputs["finance_subgroup_hydrogen.LCOH"][0]
    final_lcoh = cases[-1].outputs["finance_subgroup_hydrogen.LCOH"][0]

    with subtests.test("Check LCOH changed"):
        assert final_lcoh != initial_lcoh

    with subtests.test("Check total adjusted CapEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_capex_adjusted")[0], rel=1e-3
            )
            == 2667734319.98
        )
    with subtests.test("Check total adjusted OpEx"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.total_opex_adjusted")[0], rel=1e-3
            )
            == 72718135.62
        )

    with subtests.test("Check minimum total hydrogen produced"):
        assert (
            pytest.approx(
                model.prob.get_val("electrolyzer.total_hydrogen_produced", units="kg/year")[0],
                abs=15000,
            )
            == 60500000
        )


def test_paper_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "06_custom_tech")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "wind_plant_paper.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check LCOP"):
        assert pytest.approx(model.prob.get_val("paper_mill.LCOP"), rel=1e-3) == 51.733275


@unittest.skipUnless(importlib.util.find_spec("mcm") is not None, "mcm is not installed")
def test_wind_wave_doc_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "09_co2/direct_ocean_capture")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "offshore_plant_doc.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check LCOC"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_co2.LCOC")[0], rel=1e-3)
            == 2.26955589
        )

    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_electricity.LCOE")[0], rel=1e-3)
            == 0.330057
        )


@unittest.skipUnless(importlib.util.find_spec("mcm") is not None, "mcm is not installed")
def test_splitter_wind_doc_h2_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "17_splitter_wind_doc_h2")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "offshore_plant_splitter_doc_h2.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_hydrogen.LCOH")[0], rel=1e-3)
            == 10.25515911
        )

    with subtests.test("Check LCOC"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_co2.LCOC")[0], rel=1e-3)
            == 14.19802243
        )

    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_electricity.LCOE")[0], rel=1e-3)
            == 0.1385128
        )


def test_hydro_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "07_run_of_river_plant")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "07_run_of_river.yaml")

    # Run the model
    model.run()

    model.post_process()

    print(model.prob.get_val("finance_subgroup_default.LCOE"))

    # Subtests for checking specific values
    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_default.LCOE"), rel=1e-3)
            == 0.17653979
        )


def test_hybrid_energy_plant_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "11_hybrid_energy_plant")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "wind_pv_battery.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check LCOE"):
        assert model.prob.get_val("finance_subgroup_default.LCOE", units="USD/MW/h")[0] < 83.2123


def test_asu_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "13_air_separator")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "13_air_separator.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    with subtests.test("Check LCON"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_default.LCON", units="USD/kg")[0],
                abs=1e-4,
            )
            == 0.309041977334972
        )


def test_hydrogen_dispatch_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "14_wind_hydrogen_dispatch")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "inputs" / "h2i_wind_to_h2_storage.yaml")

    model.run()

    model.post_process()

    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_elec.LCOE", units="USD/MW/h")[0],
                rel=1e-5,
            )
            == 105.75426
        )

    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_h2.LCOH", units="USD/kg")[0],
                rel=1e-5,
            )
            == 5.6540332
        )


@unittest.skipUnless(importlib.util.find_spec("mcm") is not None, "mcm is not installed")
def test_wind_wave_oae_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "09_co2/ocean_alkalinity_enhancement")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "offshore_plant_oae.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    # Note: These are placeholder values. Update with actual values after running the test
    # when MCM package is properly installed and configured
    with subtests.test("Check LCOC"):
        assert pytest.approx(model.prob.get_val("finance_subgroup_co2.LCOC"), rel=1e-3) == 37.82

    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_electricity.LCOE"), rel=1e-3)
            == 0.367
        )


@unittest.skipUnless(importlib.util.find_spec("mcm") is not None, "mcm is not installed")
def test_wind_wave_oae_example_with_finance(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "09_co2/ocean_alkalinity_enhancement_financials")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "offshore_plant_oae.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Subtests for checking specific values
    # Note: These are placeholder values. Update with actual values after running the test
    # when MCM package is properly installed and configured
    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(model.prob.get_val("finance_subgroup_electricity.LCOE"), rel=1e-3)
            == 0.09180
        )

    with subtests.test("Check Carbon Credit"):
        assert pytest.approx(model.prob.get_val("oae.carbon_credit_value"), rel=1e-3) == 569.5


def test_natural_gas_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "16_natural_gas")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "natgas.yaml")

    # Run the model

    model.run()

    model.post_process()

    # Subtests for checking specific values

    with subtests.test("Check CapEx"):
        capex = model.prob.get_val("natural_gas_plant.CapEx")[0]
        assert pytest.approx(capex, rel=1e-6) == 1e8

    with subtests.test("Check OpEx"):
        fopex = model.prob.get_val("natural_gas_plant.OpEx")[0]
        vopex = model.prob.get_val("natural_gas_plant.VarOpEx")[0]
        opex = fopex + vopex
        assert pytest.approx(opex, rel=1e-6) == 1292000.0

    with subtests.test("Check total electricity produced"):
        total_electricity = model.prob.get_val(
            "finance_subgroup_default.electricity_sum.total_electricity_produced"
        )[0]
        assert pytest.approx(total_electricity, rel=1e-6) == 1.168e8

    with subtests.test("Check opex adjusted ng_feedstock"):
        opex_ng_feedstock = model.prob.get_val(
            "finance_subgroup_default.varopex_adjusted_ng_feedstock"
        )[0]
        assert pytest.approx(opex_ng_feedstock, rel=1e-6) == 3589463.41463415

    with subtests.test("Check capex adjusted natural_gas_plant"):
        capex_ng_plant = model.prob.get_val(
            "finance_subgroup_default.capex_adjusted_natural_gas_plant"
        )[0]
        assert pytest.approx(capex_ng_plant, rel=1e-6) == 97560975.60975611

    with subtests.test("Check opex adjusted natural_gas_plant"):
        fopex_ng_plant = model.prob.get_val(
            "finance_subgroup_default.opex_adjusted_natural_gas_plant"
        )[0]
        vopex_ng_plant = model.prob.get_val(
            "finance_subgroup_default.varopex_adjusted_natural_gas_plant"
        )[0]
        opex_ng_plant = vopex_ng_plant + fopex_ng_plant
        assert pytest.approx(opex_ng_plant, rel=1e-6) == 1260487.80487805

    with subtests.test("Check total adjusted CapEx"):
        total_capex = model.prob.get_val("finance_subgroup_default.total_capex_adjusted")[0]
        assert pytest.approx(total_capex, rel=1e-6) == 97658536.58536586

    with subtests.test("Check total adjusted OpEx"):
        total_fopex = model.prob.get_val("finance_subgroup_default.total_opex_adjusted")[0]
        total_vopex = model.prob.get_val("finance_subgroup_default.total_varopex_adjusted")[0]
        total_opex = total_fopex + total_vopex
        assert pytest.approx(total_opex, rel=1e-6) == 4849951.2195122

    with subtests.test("Check LCOE"):
        lcoe = model.prob.get_val("finance_subgroup_default.LCOE")[0]
        assert pytest.approx(lcoe, rel=1e-6) == 0.12959097

    # Test feedstock-specific values
    with subtests.test("Check feedstock output"):
        ng_output = model.prob.get_val("ng_feedstock_source.natural_gas_out")
        # Should be rated capacity (100 MMBtu) for all timesteps
        assert all(ng_output == 100.0)

    with subtests.test("Check feedstock consumption"):
        ng_consumed = model.prob.get_val("ng_feedstock.natural_gas_consumed")
        # Total consumption should match what the natural gas plant uses
        expected_consumption = (
            model.prob.get_val("natural_gas_plant.electricity_out") * 7.5
        )  # Convert MWh to MMBtu using heat rate
        assert pytest.approx(ng_consumed.sum(), rel=1e-3) == expected_consumption.sum()

    with subtests.test("Check feedstock CapEx"):
        ng_capex = model.prob.get_val("ng_feedstock.CapEx")[0]
        assert pytest.approx(ng_capex, rel=1e-6) == 100000.0  # start_up_cost

    with subtests.test("Check feedstock OpEx"):
        ng_opex = model.prob.get_val("ng_feedstock.VarOpEx")[0]
        # OpEx should be annual_cost (0) + price * consumption
        ng_consumed = model.prob.get_val("ng_feedstock.natural_gas_consumed")
        expected_opex = 4.2 * ng_consumed.sum()  # price = 4.2 $/MMBtu
        assert pytest.approx(ng_opex, rel=1e-6) == expected_opex


def test_wind_solar_electrolyzer_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "15_wind_solar_electrolyzer")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "15_wind_solar_electrolyzer.yaml")
    model.run()

    model.post_process()
    with subtests.test("Check LCOE"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_electricity.LCOE", units="USD/MW/h")[0],
                rel=1e-5,
            )
            == 53.9306558
        )

    with subtests.test("Check LCOH"):
        assert (
            pytest.approx(
                model.prob.get_val("finance_subgroup_hydrogen.LCOH", units="USD/kg")[0],
                rel=1e-5,
            )
            == 5.3277923
        )

    wind_generation = model.prob.get_val("wind.electricity_out", units="kW")
    solar_generation = model.prob.get_val("solar.electricity_out", units="kW")
    total_generation = model.prob.get_val("combiner.electricity_out", units="kW")
    total_energy_to_electrolyzer = model.prob.get_val("electrolyzer.electricity_in", units="kW")
    with subtests.test("Check combiner output"):
        assert (
            pytest.approx(wind_generation.sum() + solar_generation.sum(), rel=1e-5)
            == total_generation.sum()
        )
    with subtests.test("Check electrolyzer input power"):
        assert pytest.approx(total_generation.sum(), rel=1e-5) == total_energy_to_electrolyzer.sum()


def test_electrolyzer_om_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "10_electrolyzer_om")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "electrolyzer_om.yaml")

    model.run()

    lcoe = model.prob.get_val("finance_subgroup_electricity.LCOE", units="USD/MW/h")[0]
    lcoh_with_lcoh_finance = model.prob.get_val(
        "finance_subgroup_hydrogen.LCOH_lcoh_financials", units="USD/kg"
    )[0]
    lcoh_with_lcoe_finance = model.prob.get_val(
        "finance_subgroup_hydrogen.LCOH_lcoe_financials", units="USD/kg"
    )[0]
    with subtests.test("Check LCOE"):
        assert pytest.approx(lcoe, rel=1e-5) == 39.98869
    with subtests.test("Check LCOH with lcoh_financials"):
        assert pytest.approx(lcoh_with_lcoh_finance, rel=1e-5) == 13.0954678
    with subtests.test("Check LCOH with lcoe_financials"):
        assert pytest.approx(lcoh_with_lcoe_finance, rel=1e-5) == 8.00321771


def test_wind_battery_dispatch_example(subtests):
    # Change the current working directory to the example's directory
    os.chdir(EXAMPLE_DIR / "19_wind_battery_dispatch")

    # Create a H2Integrate model
    model = H2IntegrateModel(Path.cwd() / "wind_battery_dispatch.yaml")

    # Run the model
    model.run()

    model.post_process()

    # Test battery storage functionality
    with subtests.test("Check battery SOC bounds"):
        soc = model.prob.get_val("battery.electricity_soc")
        # SOC should stay within configured bounds (10% to 100%)
        assert all(soc >= 0.1)
        assert all(soc <= 1.0)

    with subtests.test("Check wind generation"):
        # Wind should generate some electricity
        wind_electricity = model.prob.get_val("wind.electricity_out")
        assert wind_electricity.sum() > 0
        # Wind electricity should match battery input (direct connection)
        battery_electricity_in = model.prob.get_val("battery.electricity_in")
        assert pytest.approx(wind_electricity.sum(), rel=1e-6) == battery_electricity_in.sum()

    with subtests.test("Check demand satisfaction"):
        electricity_out = model.prob.get_val("battery.electricity_out", units="MW")
        # Battery output should try to meet the 5 MW constant demand
        # Average output should be close to demand when there's sufficient generation
        assert electricity_out.mean() > 4.20  # MW

    # Subtest for LCOE
    with subtests.test("Check LCOE value"):
        lcoe = model.prob.get_val("finance_subgroup_electricity.LCOE")[0]
        assert pytest.approx(lcoe, rel=1e-6) == 0.07801723344476236

    # Subtest for total electricity produced
    with subtests.test("Check total electricity produced"):
        total_electricity = model.prob.get_val(
            "finance_subgroup_electricity.electricity_sum.total_electricity_produced"
        )[0]
        assert pytest.approx(total_electricity, rel=1e-6) == 62797265.9296355

    # Subtest for electricity curtailed
    with subtests.test("Check electricity curtailed"):
        electricity_curtailed = np.linalg.norm(model.prob.get_val("battery.electricity_curtailed"))
        assert pytest.approx(electricity_curtailed, rel=1e-6) == 412531.73840450746

    # Subtest for missed load
    with subtests.test("Check electricity missed load"):
        electricity_missed_load = np.linalg.norm(
            model.prob.get_val("battery.electricity_missed_load")
        )
        assert pytest.approx(electricity_missed_load, rel=1e-6) == 165604.70758669
