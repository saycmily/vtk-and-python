class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms)
        alroom = set(range(n))
        alroom.remove(0)
        nood = rooms[0]
        while nood:
            r = nood.pop(0)
            if r in alroom:
                alroom.remove(r)
                nood += rooms[r]
        if len(alroom) == 0:
            return True
        return False
