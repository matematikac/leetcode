strs = ['a','abbb']#["flower","flow","flight"]

result = ''

def is_in_all(ch , position, s):
    for element in s:
        if len(element) < position+1:
            return False
        elif ch != element[position]:
            return False
    return True

k = 0
while k < len(strs[0]):
    if is_in_all(strs[0][k], k, strs):
        result += strs[0][k]
        k += 1
    else:
        break
if len(result) == 0:
    print('" "')
else:
    print(result)