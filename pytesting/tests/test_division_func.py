from utils import division
import pytest


@pytest.mark.parametrize('a, b, result', [(2, 1, 2),
                                          (10, 5, 2),
                                          (3, -1, -3), ])
def test_division_good(a, b, result):
    assert division(a, b) == result


@pytest.mark.parametrize('divider, exception', [(0, ZeroDivisionError),
                                                ('2', TypeError), ])
def test_exceptions(divider, exception):
    with pytest.raises(exception):
        division(10, divider)
