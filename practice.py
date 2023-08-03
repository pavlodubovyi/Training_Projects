from functools import reduce


def amount_payment(payment):

    positive_payment_list = filter(lambda x: x > 0, payment)
    return reduce(lambda x, y: x + y, positive_payment_list)
    

payment = [1, -3, 4, 2, 3, -7, 5]

print(amount_payment(payment))