from pathlib import Path

import openmdao.api as om
from pytest import fixture

from h2integrate import RESOURCE_DEFAULT_DIR
from h2integrate.resource.wind.nrel_developer_wtk_api import WTKNRELDeveloperAPIWindResource


@fixture
def plant_simulation_utc_start():
    plant = {
        "plant_life": 30,
        "simulation": {
            "dt": 3600,
            "n_timesteps": 8760,
            "start_time": "01/01/1900 00:30:00",
            "timezone": 0,
        },
    }
    return plant


@fixture
def plant_simulation_nonutc_start():
    plant = {
        "plant_life": 30,
        "simulation": {
            "dt": 3600,
            "n_timesteps": 8760,
            "start_time": "01/01 00:30:00",
            "timezone": -6,
        },
    }
    return plant


@fixture
def site_config():
    site = {
        "latitude": 34.22,
        "longitude": -102.75,
        "resources": {
            "wind_resource": {
                "resource_model": "wind_toolkit_v2_api",
                "resource_parameters": {
                    "latitude": 35.2018863,
                    "longitude": -101.945027,
                    "resource_year": 2012,  # 2013,
                },
            }
        },
    }
    return site


def test_wind_resource_loaded_from_default_dir(plant_simulation_utc_start, site_config, subtests):
    plant_config = {
        "site": site_config,
        "plant": plant_simulation_utc_start,
    }

    prob = om.Problem()
    comp = WTKNRELDeveloperAPIWindResource(
        plant_config=plant_config,
        resource_config=plant_config["site"]["resources"]["wind_resource"]["resource_parameters"],
        driver_config={},
    )
    prob.model.add_subsystem("resource", comp)
    prob.setup()
    prob.run_model()
    wtk_data = prob.get_val("resource.wind_resource_data")

    wind_dir = RESOURCE_DEFAULT_DIR / "wind"
    with subtests.test("filepath for data was found where expected"):
        assert Path(wtk_data["filepath"]).exists()
        assert Path(wtk_data["filepath"]).parent == wind_dir

    temp_keys = [k for k in list(wtk_data.keys()) if "temperature" in k]
    wdir_keys = [k for k in list(wtk_data.keys()) if "wind_direction" in k]
    wspd_keys = [k for k in list(wtk_data.keys()) if "wind_speed" in k]
    pressure_keys = [k for k in list(wtk_data.keys()) if "pressure" in k]

    with subtests.test("more than 3 wind speed keys"):
        assert len(wspd_keys) > 0
    with subtests.test("same number of wind direction keys and wind speed"):
        assert len(wdir_keys) == len(wspd_keys)
    with subtests.test("same number of temperature keys and wind speed"):
        assert len(temp_keys) == len(wspd_keys)
    with subtests.test("3 heights for pressure data"):
        assert len(pressure_keys) == 3

    data_keys = temp_keys + wdir_keys + wspd_keys + pressure_keys
    with subtests.test("resource data is 8760 in length"):
        assert all(len(wtk_data[k]) == 8760 for k in data_keys)
