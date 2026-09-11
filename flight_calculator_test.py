from flight_calculator import calculate_flight_time, flight_time_table

"""
Tests for calculate_flight_time
"""
def test_calculate_flight_time_with_zero_payload():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_with_typical_payload():
    assert calculate_flight_time(500) == 130


def test_calculate_flight_time_does_not_return_negative_value():
    assert calculate_flight_time(2000) == 0


def test_calculate_flight_time_with_negative_payload_raises_value_error():
    try:
        calculate_flight_time(-1)
        assert False, "Expected ValueError for a negative payload"
    except ValueError:
        pass



"""
Tests for flight_time_table
"""    
def test_flight_time_table_generates_expected_entries():
    assert flight_time_table(1000, 250) == [
        (0, 180),
        (250, 155.0),
        (500, 130.0),
        (750, 105.0),
        (1000, 80.0),
    ]


def test_flight_time_table_with_zero_maximum_weight():
    assert flight_time_table(0, 100) == [(0, 180)]


def test_flight_time_table_with_negative_maximum_weight_returns_empty_list():
    assert flight_time_table(-100, 100) == []


def test_flight_time_table_with_zero_step_raises_value_error():
    try:
        flight_time_table(100, 0)
        assert False, "Expected ValueError when step_grams is zero"
    except ValueError:
        pass