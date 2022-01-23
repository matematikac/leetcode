l1 = [10]
l2 =[31]
number1=0
number2=0
for i in range(len(l1)):
    number1+=l1[len(l1)-i-1]*pow(10,len(l1)-i-1)
for i in range(len(l2)):
    number2+=l2[len(l2) - i - 1]*pow(10, len(l2) - i - 1)

number=number1+number2
k=0
while number>0:
   ost=number%pow(10,k+1)
   number=number-ost
   k+=1
number=number1+number2
result=[0]*k
k=0
while number>0:
   ost=number%pow(10,k+1)
   number=number-ost
   result[k]=int((ost/pow(10,k)))
   k+=1

print(result)