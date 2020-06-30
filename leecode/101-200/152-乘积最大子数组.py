class Solution:
    def sub(self, x, y):
        return x*y

    def maxProduct(self, nums) -> int:
        from functools import reduce
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        for i in range(l):
            if nums[i] == 0:
                return max(self.maxProduct(nums[:i]), self.maxProduct(nums[i+1:]), 0)
        n = 0
        for i in range(l):
            if nums[i] < 0:
                n += 1
        if n & 1:
            a, b = 0, l-1
            for k in range(l):
                if nums[k] < 0:
                    a = k
                    break
            while b > a:
                if nums[b] < 0:
                    break
                b -= 1
            if b == a:
                if a == 0:
                    return reduce(self.sub, nums[a+1:])
                elif a == l-1:
                    return reduce(self.sub, nums[:a])
                else:
                    return max(reduce(self.sub, nums[:a]), reduce(self.sub, nums[a+1:]))
            else:
                return max(reduce(self.sub, nums[a+1:]), reduce(self.sub, nums[:b]))
        else:
            return reduce(self.sub, nums)
