import math
import random


def make_random_power_definite_integral():
    a = random.randint(-5, 4)
    b = random.randint(a + 1, 5)

    n = random.randint(2, 5)

    num = b ** (n + 1) - a ** (n + 1)
    den = n + 1

    gcd = math.gcd(num, den)

    num //= gcd
    den //= gcd

    print(a, b, n, num, den)


make_random_power_definite_integral()
