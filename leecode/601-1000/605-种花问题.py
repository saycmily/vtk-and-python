def canPlaceFlowers(flowerbed, n) -> bool:
    l = len(flowerbed)
    if l == 1:
        if flowerbed[0] == 0:
            return n <= 1
        return n <= 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1
    for i in range(1, l-1):
        if flowerbed[i] == 1:
            continue
        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        n -= 1
    return True if n <= 0 else False


flowerbed = [0, 0, 1, 0, 1]
print(canPlaceFlowers(flowerbed, 1))
