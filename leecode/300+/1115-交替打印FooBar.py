import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.s2.acquire()
            printBar()
            self.s1.release()
