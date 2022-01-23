s = "abcadafghijtbcbcbb" #


def check(str):
    l = []
    for element in str:
        l.append(ord(element))
    ord_set = set(l)
    if len(ord_set) == len(str):
        return True
    else:
        return False

def max_substring(str):
    max_sub = str[0]
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if check(substring) and len(substring) > len(max_sub):
                max_sub = substring
    return max_sub
print(max_substring(s))

