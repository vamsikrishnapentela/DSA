def array(nums):
    a=[]
    n=len(nums)
    for i in range(n):
        count=0
        for j in range(n):
            if nums[j]==nums[i]:
                count+=1
        if count == 1:
            a.append(nums[i])
    return a
print(array([1,2,1,2,3]))

#Better
def find_non_repeating(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    
    return [num for num in nums if num not in duplicates]

print(find_non_repeating([1, 2, 1, 2, 3]))  # [3]