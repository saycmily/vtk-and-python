# a = ["abcw","baz","foo","bar","xtfn","abcdef"]
# a.sort(key=len, reverse=True)
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        ans = []
        for a in words:
            for b in words:
                f = set(a) & set(b)
                if not f:
                    ans.append(len(a)*len(b))
        if ans:
            return max(ans)
        return 0
