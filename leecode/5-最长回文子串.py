# def longestPalindrome(self, s: str) -> str:
#     answer = str()
#     if len(s) != 0:
#         answer = s[0]
#         for i in range(len(s)-1):
#             for j in range(i+1,len(s)):
#                 s1 = s[i:j+1]
#                 if s1 == s1[::-1]:
#                     if len(answer) < len(s1):
#                         answer = s1
#     return answer


def longestPalindrome(self, s):
    if len(s) <= 1:
        return s
    answer = ""
    new_s = "#"
    for i in s:
        new_s += i + "#"
    strip = 1
    for i in range(1, len(new_s)-2):
        # 使用 \ 衔接多行代码
        while i - strip >= 0 and i + strip < len(new_s) \
         and new_s[i-strip:i+strip+1] == new_s[i-strip:i+strip+1][::-1]:
            answer = new_s[i-strip:i+strip+1]
            strip += 1
        # while i - strip >= 0 and i + strip < len(new_s):
        #     if new_s[i-strip:i+strip+1] == new_s[i-strip:i+strip+1][::-1]:
        #         answer = new_s[i-strip:i+strip+1]
        #         strip += 1
        # 增加if会提高复杂度
    a = ""
    for i in answer:
        if i != '#':
            a += i
    return a
