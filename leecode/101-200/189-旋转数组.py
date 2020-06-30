def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # 三次翻转
    k = k % len(nums)
    # k值有限制
    # nums[:] = nums[::-1]
    # nums[:k] = nums[k-1::-1]
    # nums[k:] = nums[-1:k-1:-1]

    # 切片
    # nums[:-k] = nums[:-k][::-1]
    # nums[-k:] = nums[-k:][::-1]
    # nums[:] = nums[::-1]

    # reverse函数
    nums[:-k] = reversed(nums[:-k])
    nums[-k:] = reversed(nums[-k:])
    nums[:] = reversed(nums[:])
    print(nums)


nums = [1, 2, 3, 4, 5, 6]
k = 2
rotate(nums, k)
