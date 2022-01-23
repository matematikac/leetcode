head = [1,2,3,4,7]


if len(head) <= 1:
    print(head)
else:
    for i in range(len(head)):
        if i%2 == 0 :
            temp = head[i]
            if (i+1) < len(head):
                head[i] = head[i+1]
                head[i+1] = temp
print(head)