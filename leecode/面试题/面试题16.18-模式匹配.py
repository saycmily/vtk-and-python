class Solution:
    def patternMatching(self, p, s):
        from collections import Counter
        p1 = Counter(p)
        a = p1.get('a', 0)
        b = p1.get('b', 0)
        n = len(s)
        if a == b == 0:
            if n == 0:
                return True
            else:
                return False
        if n == 0:
            if a == 0 or b == 0:
                return True
            else:
                return False
        if a == 0 or b == 0:
            if n % (a+b) == 0:
                c = n // (a+b)
                for i in range(a+b-1):
                    if s[i*c:i*c+c-1] != s[i*c+c:i*c+2*c-1]:
                        return False
                return True
            else:
                return False
        for i in range(n // a+1):
            d1 = (n-a*i) // b
            d2 = (n-a*i) % b
            f = 0
            if d2 == 0:
                ea = set()
                eb = set()
                j1 = 0
                j2 = 0
                while j1 < a+b:
                    if p[j1] == 'a':
                        ea.add(s[j2:j2+i])
                        j2 += i
                    else:
                        eb.add(s[j2:j2+d1])
                        j2 += d1
                    j1 += 1
                    if len(ea) > 1 or len(eb) > 1:
                        f = 1
                        break
                if f == 1:
                    continue
                else:
                    return True
        return False
