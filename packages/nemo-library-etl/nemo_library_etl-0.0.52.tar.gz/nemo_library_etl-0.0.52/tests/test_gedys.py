from pathlib import Path

from nemo_library import NemoLibrary
from nemo_library_etl.adapter.gedys.flow import gedys_flow

COMPANY_JOINED = "gedys_Company_Joined"

def test_gedys() -> None:

    try:
        gedys_flow()
    except Exception as e:
        assert False, f"Gedys flow failed with exception: {e}"

    # check if the flow created the expected files
    # we expect 2 folders in etl/gedys: extract, transform

    etl_path = Path(__file__).parent / "etl" / "gedys"
    assert etl_path.exists(), f"ETL path {etl_path} does not exist"
    extract_path = etl_path / "extract"
    transform_path = etl_path / "transform"
    assert extract_path.exists(), f"Extract path {extract_path} does not exist"
    assert transform_path.exists(), f"Transform path {transform_path} does not exist"

    # check whether the project exsists
    nl = NemoLibrary()
    project_id = nl.getProjectID(COMPANY_JOINED)
    assert (
        project_id is not None
    ), f"Project {COMPANY_JOINED} does not exist in Nemo"

    # get columns of the project
    columns = nl.getColumns(projectname=COMPANY_JOINED)
    column_internal_names = [col.internalName for col in columns]

    assert "company_number" in column_internal_names, "Column company_number not in project"