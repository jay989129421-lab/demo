"""Assignment 3: Check whether a triangle is right-angled (using a function)."""


def is_right_angled(a, b, c):
    """Return True if the sides form a right-angled triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    x, y, z = sorted([a, b, c])          # z is the longest side (hypotenuse)
    if x + y <= z:                       # not a valid triangle
        return False
    return abs(x**2 + y**2 - z**2) < 1e-9   # Pythagoras theorem


a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))

if is_right_angled(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is NOT a right-angled triangle.")
