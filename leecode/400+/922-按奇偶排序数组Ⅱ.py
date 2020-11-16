class Solution:
    def sortArrayByParityII(self, A: list[int]) -> list[int]:
        n = len(A)
        B = A[:]
        ou, ji = 0, 1
        for i in A:
            if i % 2:
                B[ji] = i
                ji += 2
            else:
                B[ou] = i
                ou += 2
        return B
