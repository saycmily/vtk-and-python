class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sta = n / 3
        num_dict = {}
        res = []
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
                if num_dict[i] > sta and i not in res:
                    res.append(i)
            else:
                num_dict[i] = 1
                if 1 > sta:
                    res.append(i)
        return res
