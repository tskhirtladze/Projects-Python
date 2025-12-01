import pytest
import math
from source.shapes import Square


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (9, 81), (11, 121), (2, 4)])
def test_multiple_square(side_length, expected_area):
    assert Square(side_length).area() == expected_area
