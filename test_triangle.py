from triangle import classify_triangle


def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"
