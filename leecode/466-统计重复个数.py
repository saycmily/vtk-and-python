class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        indexr = [0] * (len(s2) + 1)
        countr = [0] * (len(s2) + 1)
        idx, cnt = 0, 0
        for i in range(1, n1 + 1):
            for j in range(len(s1)):
                if s1[j] == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        idx = 0
                        cnt += 1
            countr[i] = cnt
            indexr[i] = idx

            for k in range(i):
                if indexr[k] == idx:
                    prev_count = countr[k]
                    pattern_count = (n1 - k) // (i - k) * (countr[i] - countr[k])
                    remain_count = countr[k + (n1 - k) % (i - k)] - countr[k]
                    return (prev_count + pattern_count + remain_count) // n2
        return countr[n1] // n2
