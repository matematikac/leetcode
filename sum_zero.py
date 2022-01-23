nums = [4,-2,-9,9,7,9,10,-15,4,-9,-9,8,-6,7,-7,-2,4,-9,-7,-11,13,9,5,-8,10,8,-6,-1,-2,-6,6,-12,7,4,4,-9,-1,-1,-8,10,5,-10,-5,7,12,4,12,-6,10,-10,-2,8,7,10,7,2,-5,9,-14,9,-12,-1,4,2,11,-15,9,-13,-1,-14,4,12,-9,-15,-4,10,4,-7,-11,-9,-1,-6,14,-9,-10,-1,0,-8,-7,-6,8,-12,0,-3,5,-4,-11,-1,-10,4,-8,10,-7,-10,2,4,-14]#[-1,0,1,2,-1,-4]

result = []
sum = 0

def sortiraj(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1,len(nums)):
            sum = nums[i]+nums[j]+nums[k]
            if sum == 0 :
                result.append(sortiraj([ nums[i],nums[j],nums[k]]))

no_dupes = [x for n, x in enumerate(result) if x not in result[:n]]

for el in no_dupes:
    print(el)