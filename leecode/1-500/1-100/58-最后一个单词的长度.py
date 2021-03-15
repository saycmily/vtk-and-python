def lengthOfLastWord(s):
    s = s.rstrip()
    x = s.split(' ')[-1]
    return len(x)


print(lengthOfLastWord(" a "))
