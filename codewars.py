def multiiter(*params):
    if len(params) == 1:
        n = *params
        for i in range(int(params)):
            yield tuple(i)
    elif len(params) == 2:
        for i in [params][0]:
            for j in [params][1]:
                yield (i, j)


for item in multiiter(2, 3):
    print(item)