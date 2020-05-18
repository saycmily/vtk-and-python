class Solution:
    def scheduleCourse(self, courses) -> int:
        import heapq
        courses = sorted(courses, key=lambda l: l[1])
        q = []
        d = 0
        for c in courses:
            if d + c[0] <= c[1]:
                d += c[0]
                heapq.heappush(q, -c[0])
            elif q and -q[0] > c[0]:
                d += c[0] + heapq.heappop(q)
                heapq.heappush(q, -c[0])
        return len(q)
