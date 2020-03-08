def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    c = bin(a + b)
    return c[2:]
