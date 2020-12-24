class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        left = 0
        cur = defaultdict(int)
        res = 0
        for right, val in enumerate(s):
            cur[val] += 1
            # 找到目前最大字符个数,看该窗口是否多余翻转k个字符
            while right - left + 1 - max(cur.values()) > k:
                cur[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
