import re


def isMatch(s, p):
    # ans = str(*re.findall(p, s))
    # print(ans)
    # if ans == s:
    #     return True
    # else:
    #     return False
    ans = re.search(p, s)  # match
    if ans and ans.group() == s:
        return True
    else:
        return False


s = 'aab'
p = 'c*a*b'
print(isMatch(s, p))
