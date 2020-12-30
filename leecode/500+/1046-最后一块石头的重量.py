class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x != y:
                stones.append(y - x)
        return 0 if not stones else stones[0]
