class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return ' '.join(li)
