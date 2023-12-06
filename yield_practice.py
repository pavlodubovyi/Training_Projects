def generator_numbers(string=""):
    num_str = ""
    num_list = []
    for el in string:
        if el.isdigit():
            num_str += el
        elif not el.isdigit() and num_str:
            num_list.append(int(num_str))
            num_str = ""

    count = 0
    while count < len(num_list):
        yield num_list[count]
        count += 1


string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."


def sum_profit(string):
    summ = 0
    for num in generator_numbers(string):
        summ += num
    return summ


print(sum_profit(string))
