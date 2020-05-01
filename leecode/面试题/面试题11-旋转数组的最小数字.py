class Solution:
    def minArray(self, numbers):
        n = len(numbers)
        for i in range(n-1):
            if numbers[i] > numbers[i+1]:
                return numbers[i+1]
        return numbers[0]
