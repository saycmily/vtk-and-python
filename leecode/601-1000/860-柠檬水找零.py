class Solution:
    def lemonadeChange(self, bills) -> bool:
        koudai = {
            5: 0,
            10: 0,
        }
        for i in bills:
            if i == 5:
                koudai[5] += 1
            elif i == 10:
                if koudai[5] == 0:
                    return False
                koudai[5] -= 1
                koudai[10] += 1
            elif i == 20:
                if koudai[5] > 0 and koudai[10] > 0:
                    koudai[5] -= 1
                    koudai[10] -= 1
                elif koudai[5] >= 3:
                    koudai[5] -= 3
                else:
                    return False
        return True
