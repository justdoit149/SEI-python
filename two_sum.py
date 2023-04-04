def to_do(nums,target):
    LEN = len(nums)
    for i in range(LEN):
        for j in range(i+1,LEN):
            if nums[i] + nums[j] == target:        
                return [i,j]
            
