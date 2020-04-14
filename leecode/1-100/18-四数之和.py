def fourSum(nums, target):
    result = []
    if not nums or len(nums) < 4:
        return None
    nums.sort()
    # 数组长度
    length = len(nums)
    # 定义4个指针k，i，j，h  k从0开始遍历，i从k+1开始遍历，留下j和h，j指向i+1，h指向数组最大值
    for k in range(length - 3):
        # 当k的值与前面的值相等时忽略
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        # 获取当前最小值，如果最小值比目标值大，说明后面越来越大的值根本没戏
        min1 = nums[k] + nums[k+1] + nums[k+2] + nums[k+3]
        if min1 > target:
            break
        # 获取当前最大值，如果最大值比目标值小，说明后面越来越小的值根本没戏，忽略
        max1 = nums[k] + nums[length-1] + nums[length - 2] + nums[length - 3]
        if max1 < target:
            continue
        for i in range(k+1, length-2):
            if i > k + 1 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            h = length - 1
            min2 = nums[k] + nums[i] + nums[j] + nums[j + 1]
            if min2 > target:
                continue
            max2 = nums[k] + nums[i] + nums[h] + nums[h - 1]
            if max2 < target:
                continue
            # 开始j指针和h指针的表演，计算当前和，如果等于目标值，j++并去重，h--并去重，当当前和大于目标值时h--，当当前和小于目标值时j++
            while j < h:
                curr = nums[k] + nums[i] + nums[j] + nums[h]
                if curr == target:
                    result.append([nums[k], nums[i], nums[j], nums[h]])
                    j += 1
                    while j < h and nums[j] == nums[j - 1]:
                        j += 1
                    h -= 1
                    while j < h and i < h and nums[h] == nums[h + 1]:
                        h -= 1
                elif curr > target:
                    h -= 1
                elif curr < target:
                    j += 1
    return result
