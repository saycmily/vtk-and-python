class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.tick = capacity, 0
        self.dic = {}  # 键值对形式：key:[tick,val]

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.tick += 1
        self.dic[key][0] = self.tick
        return self.dic[key][1]

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.tick += 1
        if key in self.dic:
            self.dic[key][0] = self.tick
            self.dic[key][1] = value
        else:
            if len(self.dic) == self.cap:
                dic = sorted(self.dic.items(), key=lambda x: x[1])
                del self.dic[dic[0][0]]
            self.dic[key] = [self.tick, value]
