def array(nums):
    n=len(nums)
    freq ={}
    a=[]
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if nums[j]==nums[i]:
                count+=1
            freq[nums[i]]=count
    return a.freq(nums[i])
print(array([1,2,2,1,3,4,4,4]))