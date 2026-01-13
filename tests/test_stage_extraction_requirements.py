import pytest

from app.services.fertiirrigation_calculator import (
    fertiirrigation_calculator as calculator,
    SoilData,
    WaterData,
    CropData,
    IrrigationData,
)


def test_stage_extraction_pct_by_nutrient_affects_soil_availability():
    soil = SoilData(
        bulk_density=1.3,
        depth_cm=30,
        n_no3_ppm=20,
        n_nh4_ppm=5,
        p_ppm=15,
        k_ppm=80,
        ca_ppm=300,
        mg_ppm=40,
        s_ppm=12,
        ph=7.0,
        organic_matter_pct=2.0,
        cic_cmol_kg=15,
    )

    full_avail = calculator.calculate_adjusted_soil_availability(soil, stage_extraction_pct=100)
    stage_avail = calculator.calculate_adjusted_soil_availability(
        soil,
        stage_extraction_pct_by_nutrient={"N": 10, "P2O5": 50, "K2O": 20, "Ca": 10, "Mg": 10, "S": 10}
    )

    assert stage_avail["N"] < full_avail["N"]
    assert stage_avail["P2O5"] < full_avail["P2O5"]
    assert stage_avail["N"] / full_avail["N"] == pytest.approx(0.1, rel=0.2)
    assert stage_avail["P2O5"] / full_avail["P2O5"] == pytest.approx(0.5, rel=0.2)


def test_balance_exposes_real_and_final_deficits():
    soil = SoilData(bulk_density=1.3, depth_cm=30)
    water = WaterData()
    crop = CropData(
        name="Tomate",
        n_kg_ha=120,
        p2o5_kg_ha=60,
        k2o_kg_ha=80,
        ca_kg_ha=30,
        mg_kg_ha=20,
        s_kg_ha=15,
        custom_extraction_percent={"N": 25, "P2O5": 25, "K2O": 25, "Ca": 25, "Mg": 25, "S": 25},
    )
    irrigation = IrrigationData()

    balance = calculator.calculate_nutrient_balance(
        soil=soil,
        water=water,
        crop=crop,
        irrigation=irrigation,
        stage_extraction_pct=25,
    )

    for row in balance:
        assert row["deficit_real_kg_ha"] <= row["deficit_kg_ha"]
