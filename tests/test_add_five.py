from lib.add_five import add_five


def test_if_given_three_returns_eight():
    result = add_five(3)
    assert result== 8