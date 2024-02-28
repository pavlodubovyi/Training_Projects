def reverse_fun(n):
    elements = []
    while len(n) > 0:
        reversed_string = n[::-1]
        elements.append(reversed_string[0])
        n = reversed_string[1:]
    return "".join(elements)


print(reverse_fun("012345"))
