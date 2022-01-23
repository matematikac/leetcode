number = 9

def is_it_palindromic(num):
    temp = num
    if num < 0:
        return False
    k = 0
    while num/pow(10,k) > 1 :
        k += 1
    k -= 1 # the k is the biggest power of a number
    result = 0
    while num > 0:
        ost = num%10
        num = (num - ost)/10
        result += ost*pow(10,k) #finding a reverse integer
        k -= 1
    if int(result - temp) == 0 :
        return True

if is_it_palindromic(number):
    print('Yes')
else:
    print('No')