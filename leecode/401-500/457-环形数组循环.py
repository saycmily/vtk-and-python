class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)
        for i in range(n):
            flag = 1
            if nums[i] < 0:
                flag = -1
            nex = i
            already = set()
            already.add(i)
            while (flag > 0 and nums[nex] > 0) or (flag < 0 and nums[nex] < 0):
                if nums[nex]%n == 0:
                    break
                nex = (nex + nums[nex] % n) % n
                if nex in already and len(already) > 1:
                    return True
                already.add(nex)
                if len(already) > n or len(already) == 1:
                    break
        return False

a = Solution()
b = a.circularArrayLoop([1,1])
print(b)

