class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        r = int(leaves[0] != 'r') + int(leaves[1] != 'r')
        ry = int(leaves[0] != 'r') + int(leaves[1] != 'y')
        ryr = ry
        for i in range(2, n):
            ryr = min(ry, ryr) + int(leaves[i] != 'r')
            ry = min(r, ry) + int(leaves[i] != 'y')
            r += int(leaves[i] != 'r')
        return ryr
