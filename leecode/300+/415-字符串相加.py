class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            x = ord(num1[i]) - 48
            n1 = n1*10 + x
        for i in range(len(num2)):
            x = ord(num2[i]) - 48
            n2 = n2*10 + x
        n = n1 + n2
        return str(n)
