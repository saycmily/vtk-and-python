# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        # 找峰值
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        top = l
        l, r = 0, top
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        if mountain_arr.get(l) == target:
            return l
        l, r = top, mountain_arr.length()-1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) <= target:
                r = mid
            else:
                l = mid + 1
        return l if mountain_arr.get(l) == target else -1
