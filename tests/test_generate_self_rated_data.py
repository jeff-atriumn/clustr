import pytest
from datetime import datetime
from scripts.fake_generator import generate_self_rated_data


def test_generate_self_rated_data():
    participant_id = "test_id"
    start_date = datetime(2020, 1, 1)
    num_years = 2

    data = generate_self_rated_data(participant_id, start_date, num_years)

    assert len(data) == num_years
    assert all([item["participant_id"] == participant_id for item in data])
    assert all(["date_measured" in item for item in data])
    assert all(["status" in item for item in data])

def test_generate_self_rated_data_missing_num_years():
    participant_id = "test_id"
    start_date = datetime(2020, 1, 1)

    with pytest.raises(TypeError):
        data = generate_self_rated_data(participant_id, start_date)

def test_generate_self_rated_data_missing_start_date():
    participant_id = "test_id"
    num_years = 2

    with pytest.raises(TypeError):
        data = generate_self_rated_data(participant_id, num_years)
