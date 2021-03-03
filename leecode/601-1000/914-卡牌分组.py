def hasGroupsSizeX(self, deck):
    from math import gcd
    from functools import reduce
    from collections import Counter
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2
