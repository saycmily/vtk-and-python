class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        nums = [i for i in range(1, n+1)]
        nums = list(map(lambda x: str(x), nums))
        nums.sort()
        return list(map(lambda x: int(x), nums))