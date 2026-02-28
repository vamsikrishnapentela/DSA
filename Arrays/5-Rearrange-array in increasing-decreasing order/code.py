# Rearrange a given array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order
def array(nums):
    n=len(nums)
    nums.sort()
    mid=n//2

    first_half = nums[:mid]
    second_half = nums[mid:]
    second_half.reverse()
    return first_half+second_half

print(array([1,2,5,9,3,7]))