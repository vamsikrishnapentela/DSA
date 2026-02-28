#Brute Force
def array(nums):
    n=len(nums)
    a=[0] * n
    for i in range(n):
        a[i]=nums[n-1-i]
    return a
print(array([1,2,3,4,5]))

# Better
def array1(nums):
    n=len(nums)
    p = 0
    q = n-1
    while p < q:
        nums[p],nums[q]=nums[q],nums[p]
        p+=1
        q-=1
    return nums
print(array1([1,2,3,4,5]))