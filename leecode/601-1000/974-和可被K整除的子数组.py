class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        dic = [0 for i in range(K)]
        dic[0] = 1
        for i in range(1, len(A)):
            A[i] += A[i-1]
        for a in A:
            dic[a % K] += 1
        return sum(x*(x-1)//2 for x in dic)
