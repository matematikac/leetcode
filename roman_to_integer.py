roman = {'I':1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000,}
s = input('Insert your Roman number: ').upper()

num = 0
ind = 0
for k in range(len(s)):
    if ind != 0:
        ind = 0
        continue
    else:
        if k < (len(s) - 1):
            if roman[s[k]] < roman[s[k + 1]]:
                num += roman[s[k + 1]] - roman[s[k]]
                ind = 1
            else:
                num += roman[s[k]]
                ind = 0
        elif ind == 0:
            num +=roman[s[k]]
print(num)