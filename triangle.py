def classify_triangle(a, b, c):
    # Check the allowed side range
    if not all(1 <= x <= 200 for x in (a, b, c)):
        return "Invalid"

    # Check the triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    # Classify the triangle
    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"
