# 找出目标数组中两数和等于目标值的索引
def twoSum(self, nums, target):
    # for i in range(0,len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    num_map = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in num_map:
            return [num_map[another_num], index]
        num_map[num] = index
