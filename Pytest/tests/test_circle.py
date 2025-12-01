import pytest
from source.shapes import Circle
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)


    def teardown_method(self, method):
        print(f"Tearing down {method}")


    def test_are(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2



    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 2 * math.pi * self.circle.radius
