lists = [[1,4,5],[1,3,4],[2,6]]

result = []

for l in lists:
    for el in l:
        result.append(el)

for i in range(len(result)-1):
    for j in range(i+1,len(result)):
        if result[i]>result[j]:
            temp = result[i]
            result[i] = result[j]
            result[j] = temp

print(result)