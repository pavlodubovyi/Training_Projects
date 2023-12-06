result = None
operand = None  # number
operator = None  # math
wait_for_number = True

print("Enter the first number")

while True:
    user_input = input(">>> ")
    if user_input == "=":
        print(result)
        break  # stops the calculator and prints result (first time None, than result)

    if (
        wait_for_number
    ):  # не виконується, якщо False - весь блок, аж до else (там де пішли +-*/)
        try:
            operand = int(user_input)
        except ValueError:
            print("That was not a number. Please, try again: ")
            continue  # повертає цей мікро-цикл на початок try

        wait_for_number = False

        if (
            not result
        ):  # цей блок виконується ТІЛЬКИ в перший раз, бо if not None = True. Якщо if not True, це False і блок до наступного if не виконується
            result = operand

        # весь наступний мікроблок не виконується в перший раз, бо operator = None. Далі
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            if operand == 0:
                print("You cannot divide on zero")
                continue  # перезапускає блок від if operand == 0, доки не введеш норм число
            result /= operand
    else:  # тобто якщо if wait_for_number == True, а значить від юзера очікуємо математичну дію
        if user_input in ["+", "-", "*", "/"]:
            operator = user_input
            wait_for_number = (
                True  # і знову запускаємо цикл на цифри, пропускаємо на math
            )
        else:
            print("Wrong operator. Math sign required. Try again: ")
            # мені здається, тут має бути continue, щоб повертати знову до початку виконання мікроциклу від останнього else. Але чому працює і без continue???
