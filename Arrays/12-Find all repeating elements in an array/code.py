def array(nums):
    a=[]
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[j]==nums[i]:
                count+=1
        if count > 1 and nums[i] not in a:
            a.append(nums[i])
    return a
print(array([1,2,1,2,3]))

#Better
def find_repeating(nums):
    seen = set()
    result = set()
    
    for num in nums:
        if num in seen:
            result.add(num)
        seen.add(num)
    
    return list(result)

print(find_repeating([1, 2, 1, 2, 3]))  # [1, 2]