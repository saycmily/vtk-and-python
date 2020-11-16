class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        additional = []
        for i in arr1:
            if i not in arr2:
                additional.append(i)
        ans = []
        for i in arr2:
            n = arr1.count(i)
            ans.extend([i]*n)
        ans.extend(sorted(additional))
        return ans
