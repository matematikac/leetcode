number = int(input("Insert your number: "))

l_digits = []

if number > pow(2,31)-1 or number < -pow(2,31):
    print("Your number is out of range!")
    exit()

sign = 0
if number < 0:
    number = -1*number
    sign = 1

while number != 0:
    ost = int(number%10)
    l_digits.append(str(ost))
    number = (number-ost)/10

if sign == 0:
    print(''.join(l_digits))
else:
    print('-'+''.join(l_digits))