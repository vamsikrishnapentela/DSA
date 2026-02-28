def array(nums):
    target=7
    n=len(nums)
    min_len=float('inf')
    for i in range(0,n):
        s=0
        for j in range(i,n):
            s=s+nums[j]
            if s >= target:
                min_len=min(min_len,j-i+1)
                break
    return 0 if min_len==float('inf') else min_len
        
print(array([2,3,1,2,4,3]))