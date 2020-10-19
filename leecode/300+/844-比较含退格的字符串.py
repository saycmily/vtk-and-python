class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        resS, resT = [], []
        for i in S:
            if i == '#':
                if resS:
                    resS.pop()
            else:
                resS.append(i)
        for i in T:
            if i == '#':
                if resT:
                    resT.pop()
            else:
                resT.append(i)
        print(resS, resT)
        if resS == resT:
            return True
        return False
