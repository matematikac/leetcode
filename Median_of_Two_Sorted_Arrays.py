nums1=[1, 2]
nums2=[3, 4]


for el in nums2:
    nums1.append(el)

def sortiraj(podaci):
    for i in range(len(podaci) - 1):
        for j in range(i + 1, len(podaci)):
            if podaci[i] > podaci[j]:
                temp = podaci[i]
                podaci[i] = podaci[j]
                podaci[j] = temp
    return podaci

def medijana (podaci):
    sortiraj(podaci)
    if len(nums1) % 2 != 0:
        return nums1[int((len(nums1) - 1) / 2)]
    else:
        return (nums1[int(len(nums1) / 2)] + nums1[int(len(nums1) / 2 - 1)]) / 2

print(medijana(nums1))
        # n=len(nums1)+len(nums2)
# nums=[0]*n
# for i in range(len(nums1)):
#     nums[i]=nums1[i]
# for i in range(len(nums2)):
#     nums[len(nums1)+i]=nums2[i]
#
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]>nums[j]:
#             temp=nums[j]
#             nums[j]=nums[i]
#             nums[i]=temp
#
# if n%2==0:
#     k=int(n/2)
#     median=(nums[k-1]+nums[k])/2
# else:
#     k= int((n+1)/2)
#     median=nums[k-1]
# print(median)