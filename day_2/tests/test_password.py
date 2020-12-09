import pytest

from password import Password

@pytest.fixture
def pw():
    pw = Password()
    return pw

def test_convert_input_to_dict(pw):
    converted_dict = pw.convert_input_to_dict()
    assert type(converted_dict) is list

def test_meets_policy(pw):
    does_meet_policy = pw.meets_policy()
    assert does_meet_policy is True


