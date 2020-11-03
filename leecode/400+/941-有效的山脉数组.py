class Solution:
    def validMountainArray(self, A: list[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        direct = True
        if A[1] <= A[0]:
            return False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if not direct:
                    return False
            elif A[i] < A[i-1]:
                direct = False
            else:
                return False
        if direct:
            return False
        return True
