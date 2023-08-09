from functools import reduce

def factorial(num):
    return reduce(lambda x, y: x * y, range(1, num + 1))

def zeros(n):
    count_zeroes = 0
    power = 1
    while 5**power <= n:
        count_zeroes += n // (5**power)
        power += 1
    return count_zeroes

n = 1000
print(f"zeroes expected: {zeros(n)}")
print(len(str(factorial(n))) - len(str(factorial(n)).rstrip("0")))
