def format_phone_number(func):
    def wrapper(phone):
        if len(func(phone)) == 10:
            result = "+38" + func(phone)
        elif len(func(phone)) == 12:
            result = "+" + func(phone)
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


print(sanitize_phone_number("+38(050)123-32-34"))
