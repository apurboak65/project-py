def check():
    nums = list(map(int, input().split()))
    nums.sort()
    
    if len(nums) <= 1:
        return True
    
    diff = nums[1] - nums[0]
    
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] != diff:
            return False
    
    return True

print(check())
