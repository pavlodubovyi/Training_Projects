while True:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    while a == 0 or b == 0:
        if a == 0:
            a = int(input('Enter first number once again: '))
        elif b == 0:
            b = int(input('Enter second number once again: '))
    while b != 0:
        r = a % b
        a = b
        b = r
    print(a)