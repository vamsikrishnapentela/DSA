# Given an unsorted array, find the median of the given array.

# What is a Median?
# Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.

# Mathematically,

def array(nums):
    n=len(nums)
    nums.sort()
    mid=n//2
    print("sorted array",nums)
    if n%2!=0: #odd
        return nums[mid]
    else: #odd
        return (nums[mid-1]+nums[mid])/2
print(array([1,4,2,3,5,6]))