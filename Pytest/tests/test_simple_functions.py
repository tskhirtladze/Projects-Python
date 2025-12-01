import pytest
from source.simple_functions import add, divide
import time

def test_add():
    result = add(4, 6)
    assert result == 10


def test_divide():
    result = divide(8, 4)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_add_strings():
    result = add('I like ', 'Pycharm')
    assert result == 'I like     Pycharm'


@pytest.mark.slow
def test_very_slow():
    time.sleep(6)
    result = divide(8, 4)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert add(20, 25) == 45


@pytest.mark.xfail(reason='Can not divide by zero')
def test_divide_by_zero_broken():
    divide(10, 0)