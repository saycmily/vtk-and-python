def threeSumClosest(nums, target):
    nums.sort()
    min_sum = nums[0] + nums[1] + nums[-1]
    min_x = abs(target - min_sum)
    for i in range(len(nums)):
        low = i + 1
        high = len(nums) - 1
        while(low < high):
            sum = nums[i] + nums[low] + nums[high]
            x = abs(target - sum)
            if x == 0:
                return target
            elif sum < target:
                low += 1
            else:
                high -= 1
            if x < min_x:
                min_x = x
                min_sum = sum
    return min_sum
