class Solution:
    def isNumber(self, s: str) -> bool:
        # try:
        #     num = float(s)
        #     return True
        # except:
        #     return False
        import re
        p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
        return bool(p.match(s.strip()))
