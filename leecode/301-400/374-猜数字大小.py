# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        x = (n + 1) // 2
        while guess(x) != 0:
            if guess(x) == -1:
                n = x   
            else:
                left = x
            x = (left + n + 1) // 2
        return x
