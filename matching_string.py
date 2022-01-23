s = 'cccbbaa'
p = '.*b*a'

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
k = 0
for key in d:
    if k < len(p) and (key == p[k] or p[k] =='.') :
        if d[key] > 1 and (k+1) < len(p):
            if p[k+1] == '*':
                print('jebiga',key,p[k+1],k+1)
                k += 2
            else:
                print('nije')
        else:
            k += 1
            print(k, 'jbig')
    else:
        print('jbg',k, key)
        break

