#Brute force
def array1(num):
    num.sort()
    return num[0]

print(array1([1,2,3,4,5]))

#optimal
def array(nums):
    n=len(nums)
    min_value=nums[0]
    for i in range(n):
        if nums[i]<min_value:
            min_value=nums[i]
    return min_value
print(array([1,2,3,4,5]))