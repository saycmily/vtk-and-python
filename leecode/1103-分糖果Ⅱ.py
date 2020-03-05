def distributeCandies(self, candies, num_people):
    start = 1
    i = 0
    res = [0]*num_people
    while candies >= start:
        res[i] += start
        candies -= start
        start += 1
        i += 1
        if i == num_people:
            i = 0
    res[i] += candies
    return res
