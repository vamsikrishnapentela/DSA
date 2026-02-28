def array(nums):
    n=len(nums)
    total=0
    for i in range(n):
        total=total+nums[i]
    return total
print(array([1,2,3,4,5]))

#optimal
def array(nums):
    return sum(nums)
print(array([1,2,3,4,5]))