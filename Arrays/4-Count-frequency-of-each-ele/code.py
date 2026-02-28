def array(nums):
    n=len(nums)
    freq ={}
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if nums[j]==nums[i]:
                count+=1
            freq[nums[i]]=count
    return freq
print(array([1,2,2,1,3,4]))

#better
def array(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


print(array([1, 2, 2, 1, 3, 4]))