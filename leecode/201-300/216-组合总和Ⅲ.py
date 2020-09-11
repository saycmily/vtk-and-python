class Solution:
    def combinationSum3(self, k: int, n: int):
        def backtrack(tmp, tmp_sum=0, first=0):
            if len(tmp) == k and tmp_sum == n:  # 回溯的退出条件
                res.append(tmp.copy())
                return
            for i in range(first, 9):
                if tmp_sum + candidates[i] > n:
                    break
                tmp.append(candidates[i])
                backtrack(tmp, tmp_sum + candidates[i], i+1)
                tmp.pop()  # 记得恢复之前的状态

        res = []
        candidates = [i for i in range(1, 10)]
        backtrack([])
        return res
