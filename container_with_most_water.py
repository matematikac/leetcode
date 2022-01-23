height = [2,3,4,5,18,17,6]#[1,1]#[1,8,6,2,5,4,8,3,7]
max = 0
position1 = 0
position2 = 1
for i in range(len(height)-1):
    for j in range(i+1,len(height)):
        if height[i]>=height[j]:
            a = height[j]
        else:
            a = height[i]
        b = j - i
        area= a*b
        if max < area:
            max = area
            position1 = i
            position2 = j
print(max, position1,position2)