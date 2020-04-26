def majorityElement(self, nums):
    # from collections import Counter
    # c = Counter(nums)
    # return c.most_common(1)[0][0]
    nums.sort()
    return nums[len(nums)//2]
