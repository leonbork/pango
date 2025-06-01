import os
from main import run_pipeline
from utilities.db_helpers import DatabaseHelper


def test_run_pipeline_real_api():
    run_pipeline()

    # Check if the report was created
    assert os.path.exists("reports/discrepancy_report.csv")

    # Verify database entries were made
    db = DatabaseHelper()
    data = db.fetch_all_data()
    assert len(data) >= 1
    for row in data:
        city, temp_web, feels_web, temp_api, feels_api, avg_temp = row
        assert isinstance(temp_web, float)
        assert isinstance(temp_api, float)
        assert isinstance(avg_temp, float)
        assert -100 < temp_web < 100
        assert -100 < temp_api < 100
