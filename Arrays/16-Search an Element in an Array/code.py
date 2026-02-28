def array(nums):
    k=3
    for i in range(len(nums)):
        if nums[i]==k:
            ans=i
            break
    return "present in array",i
nums=[1,2,3,4,5]
print(array(nums))