Array=[3,4,5,6,7,8,9]
Target=9
Result=Array[0]+Array[1]
ind1=0
ind2=1
for i in range(len(Array)):
    for j in range(i+1,len(Array)):
        temp=Array[i]+Array[j]
        if abs(Target-temp)<abs(Result-Target):
            Result=temp
            ind1=i
            ind2=j



print(ind1, ind2)