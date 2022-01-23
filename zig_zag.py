s = "PAYPALISHIRING"

numRows = 3
result = []*numRows
pomeraj = 2*numRows - 2
temp = []

for index in range(numRows):
    temp += s[index]
    for k in range(index + pomeraj, len(s), pomeraj):
        if (index+ pomeraj) > pomeraj  and (index + 1) != numRows:
            temp += s[k - 2*index]
        temp += s[k]
    if (k - 2*index + pomeraj) < len(s) and (index + 1) != numRows:
        temp += s[k - 2*index + pomeraj]
    result.append(temp)
    temp = []

for l in result:
    for el in l:
        temp.append(el)

print(''.join(temp))