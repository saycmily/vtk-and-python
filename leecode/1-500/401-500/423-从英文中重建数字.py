class Solution:
    def originalDigits(self, s: str) -> str:
        ans = [0]*10
        ans[0] = s.count('z')
        ans[2] = s.count('w')
        ans[4] = s.count('u')
        ans[6] = s.count('x')
        ans[8] = s.count('g')
        ans[1] = s.count('o') - ans[0] - ans[2] - ans[4]
        ans[3] = s.count('h') - ans[8]
        ans[5] = s.count('f') - ans[4]
        ans[7] = s.count('s') - ans[6]
        ans[9] = (s.count('n') - ans[1] - ans[7]) // 2
        res = ''
        for index,value in enumerate(ans):
            res += str(index) * value
        return res
