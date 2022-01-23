nums = [0,0,1,1,1,2,2,3,3,4]
result = []
number = 0
for _ in range(10):
    ind = 0
    if _ in nums and ind==0:
        result.append(_)
        ind += 1
        number += 1
    else:
        result.append('_')
print('array of non repeat element is: {}'.format(result),'\n\n' ,'the number of different elements in array is: {}'.format(number))