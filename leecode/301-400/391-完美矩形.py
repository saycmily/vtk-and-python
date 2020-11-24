class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        # 保存所有矩形的四个点
        lookup = set()
        # 最大矩形的 左下角 右上角
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")
        area = 0
        for x, y, s, t in rectangles:

            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, s)
            y2 = max(y2, t)

            area += (t - y) * (s - x)
            # 每个矩形的四个点
            for item in [(x, y), (x, t), (s, y), (s, t)]:
                if item not in lookup:
                    lookup.add(item)
                else:
                    lookup.remove(item)
        # 只剩下四个点并且是最大矩形的左下角和右上角
        if len(lookup) != 4 or \
                (x1, y1) not in lookup or (x1, y2) not in lookup or (x2, y1) not in lookup or (x2, y2) not in lookup:
            return False
        # 面积是否满足
        return (x2 - x1) * (y2 - y1) == area
