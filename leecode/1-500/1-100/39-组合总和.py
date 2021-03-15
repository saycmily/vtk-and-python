class Solution:
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(tmp, tmp_sum=0, first=0):
            if tmp_sum == target:
                res.append(tmp.copy())
                return
            for j in range(first, n):
                if tmp_sum + candidates[j] > target:
                    break
                tmp.append(candidates[j])
                backtrack(tmp, tmp_sum + candidates[j], j)
                tmp.pop()
        backtrack([])
        return res
