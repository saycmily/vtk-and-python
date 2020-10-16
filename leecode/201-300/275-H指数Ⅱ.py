class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)

        for index, value in enumerate(citations):
            x = n - index
            if x <= value:
                return x
        return 0
