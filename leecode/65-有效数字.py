def isNumber(self, s: str) -> bool:
    # try:
    #     num = float(s)
    #     return True
    # except:
    #     return False
    s = s.strip()
    dot_seen = False
    e_seen = False
    num_seen = False
    for i, a in enumerate(s):
        if '0' <= a <= '9':  # a.isdigit():
            num_seen = True
        elif a == ".":
            if e_seen or dot_seen:
                return False
            dot_seen = True
        elif a == "e":
            if e_seen or not num_seen:
                return False
            num_seen = False
            e_seen = True
        elif a in "+-":
            if i > 0 and s[i - 1] != "e":
                return False
        else:
            return False
    return num_seen
