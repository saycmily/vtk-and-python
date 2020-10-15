class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stacka = []
        self.stackb = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stacka.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stackb:
            while self.stacka:
                self.stackb.append(self.stacka.pop())
        return self.stackb.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stackb:
            while self.stacka:
                self.stackb.append(self.stacka.pop())
        return self.stackb[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stacka and not self.stackb:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()