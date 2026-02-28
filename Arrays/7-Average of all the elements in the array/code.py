def array(nums):
    n=len(nums)
    total=0
    for i in range(n):
        total=total+nums[i]
    return total/float(n)
print(array([1,2,3,4,5]))

#optimal
def array(nums):
    n=len(nums)
    return sum(nums)/float(n)
print(array([1,2,3,4]))