def canThreePartsEqualSum(A):
    s = sum(A)
    if s % 3 != 0:
        return False
    target = s // 3
    i, n = 0, len(A)-1
    sumi = sumn = 0
    while i < n + 1:
        if sumi != target or i == 0:
            sumi += A[i]
            i += 1
        if sumn != target or n == len(A)-1:
            sumn += A[n]
            n -= 1
        if sumi == target and sumn == target and i < n+1:
            return True
    return False


print(canThreePartsEqualSum([1, -1, 1, -1]))
