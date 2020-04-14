def combinationSum(self, candidates, target):
    candidates.sort()
    n = len(candidates)
    res = []

    def helper(i, tmp_sum, tmp):
        if tmp_sum > target or i == n:
            return
        if tmp_sum == target:
            res.append(tmp)
            return
        helper(i, tmp_sum + candidates[i], tmp + [candidates[i]])
        helper(i+1, tmp_sum, tmp)
    helper(0, 0, [])
    return res
