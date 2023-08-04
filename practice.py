# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("hello", help="Bot will offer its help")
# args = parser.parse_args()

# if __name__ == "__main__":
#     pass

phone_dict = {}

name_number_str = input("Enter name and number (Name, space, number): ")
name_number_list = name_number_str.split(" ")
phone_dict.update({name_number_list[0]: name_number_list[1]})
print(phone_dict)


def format_phone_number(func):
    def wrapper(*args, **kwargs):
        if len(func(*args, **kwargs)) == 9:  # написав для польских номерів
            result = "+48" + func(*args, **kwargs)
        elif len(func(*args, **kwargs)) == 11:
            result = "+" + func(*args, **kwargs)
            return result

    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone
