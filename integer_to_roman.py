num = 1991
roman = []

k = 0 #broj cifara broja
temp = num
while num > 0:
    num = (num - num%10)/10
    k += 1

num = temp
s = ''
if k >= 4:
    for _ in range(int(num/1000)):
        s += "M"
    roman.append(s)

num = num - int(num/1000)*1000 #cifra stotine
s = ''
if int(num/100) == 9:
    roman.append("CM")
elif int(num/100) == 4:
    roman.append("CD")
elif int(num/100) >4 :
    s += 'D'
    for _ in range(5,int(num/100)):
        s += "C"
    roman.append(s)
elif int(num/100) < 5  and int(num/100) != 0:
    for _ in range(int(num/100)):
        s += "C"
    roman.append(s)

num = num - int(num/100)*100 #cifra desetice
s = ''
if int(num/10) == 9:
    roman.append("XC")
elif int(num/10) == 4:
    roman.append("XL")
elif int(num/10) > 4:
    s += 'L'
    for _ in range(5,int(num/10)):
        s += "X"
    roman.append(s)
elif int(num/10)< 5 and int(num/10) != 0:
    for _ in range(int(num/10)):
        s += "X"
    roman.append(s)

num = num - int(num/10)*10 #cifra jedinice

s = ''
if num == 9:
    roman.append("IX")
elif num == 4:
    roman.append("IV")
elif num > 4:
    s += 'V'
    for _ in range(5,num):
        s += "I"
    roman.append(s)
elif num < 5 and num != 0:
    for _ in range(num):
        s += "I"
    roman.append(s)

print(f"For integer number: {temp}, the roman number is: {''.join(roman)}")