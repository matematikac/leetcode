sentence = 'Dusmani, neka jedu govna, Zvezda je sampion sveta!'
k = 10


def find_space(s):
    for n in range(len(s)):
        if s[len(s)-1-n] == ' ':
            return s[0:len(s)-n-1]

n = 0
while (n+k) < len(sentence):
    temp = sentence[n:n+k]
    if temp[k-1] == ' ':
        print(temp)
        n += len(temp)

    else:
        temp = find_space(temp)
        n += len(temp) + 1
        print(temp)

if n < len(sentence):
    print(sentence[n:len(sentence)])