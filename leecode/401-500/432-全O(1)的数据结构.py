class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.stack:
            self.stack[key] += 1
        else:
            self.stack[key] = 1
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.stack:
            if self.stack[key] == 1:
                del self.stack[key]
            else:
                self.stack[key] -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        # if len(self.stack) == 0:
        #     return ""
        return max(self.stack.items(), key = lambda x: x[1], default = [""])[0]
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return min(self.stack.items(), key = lambda x: x[1], default = [""])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()