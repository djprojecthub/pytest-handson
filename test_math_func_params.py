import math_func
import pytest


@pytest.mark.parametrize('arg1, arg2, result', [
    (7, 3, 10),
    ('Hello', ' World', 'Hello World'),
    (10.5, 25.5, 36)
])
def test_add(arg1, arg2, result):
    # assert math_func.add(7, 3) == 10
    # result = math_func.add('Hello', ' World')
    # assert result == 'Hello World'
    # result = math_func.add(10.5, 25.5)
    # assert result == 36
    assert math_func.add(arg1, arg2) == result




