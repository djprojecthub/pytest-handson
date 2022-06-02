import math
import sys
import pytest

import math_func


@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print(math_func.add(7, 3), '=====================')


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


@pytest.mark.strings
def test_add_strings():
    result = math_func.add("Hello", "World")
    assert result == "HelloWorld"
    assert type(result) is str
    assert "Hello" in result


@pytest.mark.strings
def test_product_strings():
    assert math_func.product("Hello", 3) == "HelloHelloHello"
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
