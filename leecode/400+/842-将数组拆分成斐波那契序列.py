class Solution:
    def splitIntoFibonacci(self, S: str) -> list[int]:
        if not S:
            return False
        res = []
        n = len(S)
        def backtrack(idx):
            if idx == n and len(res) > 2:
                return True
            for i in range(idx, n):
                if S[idx] == '0' and i > idx:
                    break
                tmp = int(S[idx : i+1])
                if tmp > 2**31-1:
                    break
                tmp_n = len(res)
                if tmp_n >= 2 and tmp > res[-1] +res[-2]:
                    break
                if tmp_n <= 1 or tmp == res[-1] + res[-2]:
                    res.append(tmp)
                    if backtrack(i + 1):
                        return True
                    res.pop()
            return False

        if backtrack(0):
            return res
        return []
