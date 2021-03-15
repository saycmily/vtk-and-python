def divide(self, dividend, divisor):
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        result <<= 1
        if divisor <= dividend:
            result += 1
            dividend -= divisor
    if sign:
        result = -result
    if result <= (1 << 31) - 1:
        return result
    else:
        return (1 << 31) - 1


print(3 * 2 + 4 << 2)
