from pathlib import Path
from nemo_library_etl.adapter._utils.enums import ETLAdapter, ETLStep
from nemo_library_etl.adapter.hubspot.enums import HubSpotLoadStep
from nemo_library_etl.adapter.hubspot.flow import hubspot_flow
from nemo_library_etl.adapter._utils.file_handler import ETLFileHandler
import pandas as pd


def test_hubspot() -> None:

    try:
        hubspot_flow()
    except Exception as e:
        assert False, f"HubSpot flow failed with exception: {e}"

    # check if the flow created the expected files
    # we expect 3 folders in etl/hubspot: extract, transform, load

    etl_path = Path(__file__).parent / "etl" / "hubspot"
    assert etl_path.exists(), f"ETL path {etl_path} does not exist"
    extract_path = etl_path / "extract"
    transform_path = etl_path / "transform"
    load_path = etl_path / "load"
    assert extract_path.exists(), f"Extract path {extract_path} does not exist"
    assert transform_path.exists(), f"Transform path {transform_path} does not exist"
    assert load_path.exists(), f"Load path {load_path} does not exist"

    # check if the load folder has created 2 files:
    # - dealsforecastdeals.jsonl
    # - dealsforecastheader.jsonl

    dealsforecastdeals_file = load_path / "dealsforecastdeals.jsonl"
    dealsforecastheader_file = load_path / "dealsforecastheader.jsonl"
    assert (
        dealsforecastdeals_file.exists()
    ), f"File {dealsforecastdeals_file} does not exist"
    assert (
        dealsforecastheader_file.exists()
    ), f"File {dealsforecastheader_file} does not exist"

    # import header file
    fh = ETLFileHandler()
    header_data = fh.readJSONL(
        adapter=ETLAdapter.HUBSPOT,
        step=ETLStep.LOAD,
        entity=HubSpotLoadStep.DEALS_FORECAST_HEADER,
    )
    assert len(header_data) > 0, "Header data is empty"
    
    header_df = pd.DataFrame(header_data)
    
    # assert there are at least 1 row and not more than 4 rows with dealstage = "Unqualified lead"
    unqualified_lead_rows = header_df[header_df["dealstage"] == "Unqualified lead"]
    assert len(unqualified_lead_rows) >= 1, "There are no Unqualified lead rows"
    assert len(unqualified_lead_rows) <= 4, "There are more than 4 Unqualified lead rows"
