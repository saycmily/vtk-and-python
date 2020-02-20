import re


def myAtoi(self, str):
    s = str.lstrip()
    ans = int(*re.findall('^[\+\-]?\d+', s))
    if ans > 2**31 - 1:
        return 2**31 - 1
    elif ans < -2**31:
        return -2**31
    return ans


print(re.search('www', 'www.saycmily.com').span())  # 在起始位置匹配
