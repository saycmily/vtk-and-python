class Solution:
    def findWords(self, words):
        ans = []
        for i in words:
            ls = i.lower()
            if ls.strip('qwertyuiop') == '' or \
               ls.strip('asdfghjkl') == '' or \
               ls.strip('zxcvbnm') == '':
                ans.append(i)
        return ans
