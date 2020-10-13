class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        he = sum(nums)
        if he % 2 == 1 or n < 2:
            return False

        he = he / 2
        d = defaultdict(int)
        d[0] = 1

        for num in nums:
            for k in list(d.keys()):
                r = num + k
                if r == he:
                    return True
                d[r] = 1
            # print(d)
        return False
