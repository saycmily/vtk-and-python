from collections import Counter


def findSubstring(self, s, words):
    if not s or not words:
        return []
    # 所有给定子串的长度都一样
    one_word = len(words[0])
    # 所有子串长度的总和
    all_len = len(words) * one_word
    n = len(s)
    words = Counter(words)
    res = []
    for i in range(n - all_len + 1):
        tmp = s[i:i+all_len]
        c_tmp = []
        # 每次跳oneword长度
        for j in range(0, all_len, one_word):
            c_tmp.append(tmp[j:j+one_word])
        if Counter(c_tmp) == words:
            res.append(i)
    return res


colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(dict(c))
print(c['blue'])
del c['red']
print(list(c.elements()))
print(c.most_common(3))
# +-&|
