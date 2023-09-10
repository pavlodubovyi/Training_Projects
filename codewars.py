import math


def beeramid(bonus, price):
    if bonus <= 0:
        print(0)
    else:
        cans = bonus // price
        print(f"Cans: {cans}")
        levels = math.isqrt(cans) - math.isqrt(can)
        print(f"Levels: {levels}")


beeramid(1500, 2)
