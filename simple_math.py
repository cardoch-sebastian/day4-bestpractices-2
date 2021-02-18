"""
A collection of simple math operations
"""


def simple_add(a, b):
    """Adds two numbers together.
    Parameters
    ----------
        a : (int or float) : A real number.
        b : (int or float) : A real number
    Returns
    -------
        int or float: The sum of a and b.
    """
    return a+b


def simple_sub(a, b):
    """Subtracts two numbers.
    Parameters
    ----------
        a : (int or float) : A real number.
        b : (int or float) : A real number
    Returns
    -------
        int or float: The difference between a and b.
    """
    return a-b


def simple_mult(a, b):
    """Multiplies two numbers.
    Parameters
    ----------
        a : (int or float) : A real number.
        b : (int or float) : A real number
    Returns
    -------
        int or float: The product of a and b.
    """
    return a*b


def simple_div(a, b):
    """Divides two numbers.
    Parameters
    ----------
        a : (int or float) : A real number.
        b : (int or float) : A real number
    Returns
    -------
        int or float: The division between a and b.
    """
    return a/b


def poly_first(x, a0, a1):
    """Evaluates a first degree polynomial.
    Parameters
    ----------
        x : (int or float) : Point in the line.
        a0 : (int or float) : The intercept.
        a1 : (int or float) : The slope.
    Returns
    -------
        int or float: The y-value at point x.
    """
    return a0 + a1*x


def poly_second(x, a0, a1, a2):
    """Evaluates a second degree polynomial.
    Parameters
    ----------
        x : (int or float) : Point in the curve.
        a0 : (int or float) : The y-intercept.
        a1 : (int or float) : First degree coefficient.
        a2 : (int or float) : Second degree coefficient.
    Returns
    -------
        int or float: The y-value at point x.
    """
    return poly_first(x, a0, a1) + a2*(x**2)
