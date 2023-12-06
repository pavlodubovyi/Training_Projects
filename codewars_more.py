from math import sqrt


def squares_quantity(a: int, b: int) -> int:
    num_list = []
    result_list = []
    num = a
    while num <= b:
        num_list.append(num)
        num += 1
    for x in num_list:
        if sqrt(x) % 1 == 0:
            result_list.append(x)
    return len(result_list)


print(squares_quantity(134, 1713))
