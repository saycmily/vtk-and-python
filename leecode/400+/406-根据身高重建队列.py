class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key = lambda x: (x[0], -x[1]))
        n = len(people)
        ind = list(range(n))
        clone = [0] * n
        for ya in people:
            a = ya[1]
            b = ind[a]
            del ind[a]
            clone[b] = ya
        return clone
