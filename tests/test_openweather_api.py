import pytest
from utilities.api_helpers import ApiHelper

@pytest.fixture(scope="module")
def api():
    return ApiHelper()

def test_get_weather_data(api):
    pass


