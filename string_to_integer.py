s = '  -1212asas34'

result = ''
sign = 0
for ch in s:
    if ch ==' ':
        continue
    elif ch == '-':
        sign = 1
    elif ord(ch) < 48 or ord(ch) > 57:
        continue
    else:
        result += ch
result = int(result)
while result > pow(2,31)-1 or result < -pow(2,31):
    result = int(result/10)
if sign == 0:
    print(result)
else:
    print('-',result)


