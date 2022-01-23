head = [1,2,3,4,5]
k = 3


n = 1
temp =[]
result = []
while n*k < len(head):
    temp = head[(n-1)*k:n*k]
    for _ in range(k):
        result.append(temp[k-1-_])
    n += 1
for _ in range((n-1)*k, len(head)):
    result.append(head[_])

print(result)