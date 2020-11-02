import random
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.col = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.col:
            self.col.append(val)
            return False
        else:
            self.col.append(val)
            return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.col:
            self.col.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        n = len(self.col)
        x = random.randint(0, n-1)
        return self.col[x]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()