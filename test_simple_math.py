import simple_math
import numpy


def test_simple_add():
    assert simple_math.simple_add(2, 3) == 5


def test_simple_sub():
    assert simple_math.simple_sub(2, 3) == -1


def test_simple_mult():
    assert simple_math.simple_mult(2, 3) == 6


def test_simple_div():
    assert simple_math.simple_div(2, 3) - 0.6666666666666666 <= 1E-5


def test_poly_first():
    assert simple_math.poly_first(1, 2, 3) == 5


def test_poly_second():
    assert simple_math.poly_second(1, 2, 3, 4) == 9
