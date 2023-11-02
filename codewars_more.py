def generate_hashtag(string):

    string_list = string.title().split(" ")
    hash_string = "#" + "".join(string_list)
    if len(hash_string) > 141 or len(hash_string) == 1:
        print("False")
        return False
    return hash_string

string = "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"
generate_hashtag(string)
print(len(string))