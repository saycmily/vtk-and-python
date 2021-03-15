def getPermutation(self, n, k):
    from itertools import permutations
    tup = list(permutations(list(range(1, n+1)), n))[k-1]
    tup = list(map(str, tup))
    return ''.join(tup)
