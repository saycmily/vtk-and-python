def intToRoman(self, num):
    d = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    ans = ""
    while num > 0:
        for key in d:
            while num >= d[key]:
                num -= d[key]
                ans += key
    return ans
