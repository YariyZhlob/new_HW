import pytest


@pytest.mark.parametrize('first', (1,2), ids=['first_scenario','second_scenario','third_scenario'])
def test_sum(first, second, result):
    actual = first + second
    assert actual == result