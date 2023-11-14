import pytest
from lib.present import *

def test_present_wrap_unwrap ():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

def test_present_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_duplicate():
    present = Present()
    present.wrap (66)
    with pytest.raises(Exception) as e:
        present.wrap(666)
    message = str(e.value)
    assert message == "A contents has already been wrapped."