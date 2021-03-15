def search(self, nums, target):
    n = len(nums)
    if not nums:
        return -1
    i, j = 0, n - 1
    while i < j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        if nums[i] <= target < nums[mid] or nums[mid] < nums[i] <= target or target < nums[mid] < nums[i]:
            j = mid
        else:
            i = mid + 1
    if nums[i] == target:
        return i
    return -1
