class Solution:
    def combinationSum3(self, k: int, n: int):

        def back(candidates, cur, target):
            if len(cur) == k and target == 0:  # 回溯的退出条件
                res.append(cur.copy())
            for i in range(len(candidates)):
                # 若出现逆序，则剪枝，防止出现重复的情况例如 [1,2] [2,1]是一种
                if len(cur) > 0 and candidates[i] < cur[-1]:
                    continue
                cur.append(candidates[i])
                back(candidates[i+1:], cur, target-candidates[i])
                cur.pop()  # 记得恢复之前的状态

        res = []
        nums = [i for i in range(1, 10)]
        back(nums, [], n)
        return res
