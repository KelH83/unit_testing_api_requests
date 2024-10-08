from unittest.mock import Mock
from lib.time_error import TimeError

def test_calls_api_to_provide_time_difference_between_machine_and_api():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value ={"unixtime":1728378079}
    time_mock = Mock()
    time_mock.time.return_value = 1728378078.00
    time_error = TimeError(requester_mock, time_mock)
    assert time_error.error() == 1.0

