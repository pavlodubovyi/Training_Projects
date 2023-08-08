
def first_non_repeating_letter(s):

    count = 0
    s_lower = s.lower()
    for chr in s_lower:
        num = 0
        num = s_lower.count(chr)
        if num == 1:
            if s_lower[count] == s[count]:
                return chr
            else:
                return chr.upper()
        count += 1
    return ""

s = "sTreSS"
print(first_non_repeating_letter(s))