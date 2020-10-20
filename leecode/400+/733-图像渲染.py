class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m = len(image)
        n = len(image[0])
        z = image[sr][sc]
        if z == newColor:
            return image
        ready = list()
        ready.append((sr, sc))
        image[sr][sc] = newColor
        while ready:
            (i1, j1) = ready.pop(0)
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i1 + i
                y = j1 + j
                if 0 <= x < m and 0 <= y < n and image[x][y] == z:
                    image[x][y] = newColor
                    ready.append((x, y))
        return image
