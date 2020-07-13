class Solution:
    def spiralOrder(self, matrix):
        res = []

        def exactly(tmp):
            if len(tmp) == 0:
                return
            if len(tmp) == 1:
                res.extend(tmp[0])
                return
            res.extend(tmp[0])
            del tmp[0]
            i = 0
            while i < len(tmp):
                res.append(tmp[i][-1])
                del tmp[i][-1]
                if len(tmp[i]) == 0:
                    del tmp[i]
                    i -= 1
                i += 1
            if len(tmp) == 0:
                return
            res.extend(reversed(tmp[-1]))
            del tmp[-1]

            j = len(tmp) - 1
            while j >= 0:
                res.append(tmp[j][0])
                del tmp[j][0]
                if len(tmp[j]) == 0:
                    del tmp[j]
                j -= 1
            exactly(tmp)
        exactly(matrix)
        return res
