import re

def increment_string(string):

    if not string:
        final_string = '1'

    search_result = re.search('\d+', string[::-1])
    if not search_result:
        final_string = string + '1'
    else:
        reversed_num = search_result.group()
        last_num = reversed_num[::-1]
        print(f"last number: {last_num}")

        new_num_int = int(last_num) + 1
        new_num_str = str(new_num_int)

        str_without_end_num = string[:-len(last_num)]

        num_value = last_num.lstrip('0')
        first_zeroes = len(last_num) - len(num_value)
        print(f"first zeroes: {first_zeroes}")

        if len(num_value) == len(new_num_str):
            final_string = str_without_end_num + '0' * first_zeroes + new_num_str
        else:
            final_string = str_without_end_num + '0' * (first_zeroes - 1) + new_num_str

    return final_string


string = 'dubai090'
print(increment_string(string))

