# # from random import randint


# # def get_random_password():
    
# #     password_list = []  # generate random numbers, corresponding to ASCII table
    
# #     while len(password_list) < 8:
# #         random_num = randint(40, 126)
# #         password_list.append(random_num)

# #     password = []   # This will be the list of charachters

# #     for num in password_list:   # convert numbers from password_list to charachters
# #         num = chr(num)
# #         password.append(num)
# #         print(password)

# #     random_password = ''.join(password) # convert the list (password) to string
# #     print(random_password)      # self check
# #     return random_password
    
# def is_valid_password(password):
    
#     if len(password) != 8:
#         return False
    
#     has_upper = False
#     has_lower = False
#     has_digit = False

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
    
#     return has_upper and has_lower and has_digit
    


# password = "a1EEM+gb" 

from random import randint


def get_random_password():

    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    print(result)
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():

    count = 0
    while count < 100:
        password_at_last = get_random_password()
        if is_valid_password(password_at_last):
            return password_at_last
        count += 1
        

get_password()