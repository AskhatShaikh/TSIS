def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

nums = [1,3,0,0,7,7,2]
print(spy_game(nums))
