import math


def gcdOfStrings(str1, str2):
    # 求出最大公约数
    candidate_len = math.gcd(len(str1), len(str2))
    candidate = str1[: candidate_len]
    if str1 + str2 == str2 + str1:
        return candidate
    return ''


print(gcdOfStrings('ab', 'abab'))
