# 双指针
def removeElement(nums, val):
    i = 0
    for index, value in enumerate(nums):
        if value != val:
            nums[i] = value
            i += 1
    # 返回移除指定元素后数组大小
    return i


nums = [1, 2, 3, 3, 3, 4]
print(removeElement(nums, 3))
