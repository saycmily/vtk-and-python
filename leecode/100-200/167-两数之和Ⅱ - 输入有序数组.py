class Solution:
    def twoSum(self, numbers, target: int):
        n = len(numbers)
        i = 0
        j = n-1
        while i < j:
            mux = numbers[i] + numbers[j]
            if mux == target:
                return [i+1, j+1]
            elif mux < target:
                i += 1
            else:
                j -= 1
