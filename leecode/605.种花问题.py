def canPlaceFlowers(flowerbed, n) -> bool:
    ans = 0
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            ans = 1
        return ans >= n
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        ans += 1
        flowerbed[0] = 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        ans += 1
        flowerbed[-1] = 1

    for index, value in enumerate(flowerbed):
        if index == 0 or index == len(flowerbed)-1:
            continue
        if value == 0:
            if flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                ans += 1
                flowerbed[index] = 1
    return ans >= n


flowerbed = [0, 0, 1, 0, 1]
print(canPlaceFlowers(flowerbed, 1))
