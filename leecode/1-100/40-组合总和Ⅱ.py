class Solution:
    def combinationSum2(self, candidates, target: int):
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
                if j > first and candidates[j] == candidates[j-1]:
                    continue
                tmp.append(candidates[j])
                backtrack(tmp, tmp_sum + candidates[j], j+1)
                tmp.pop()
        backtrack([])
        return res
