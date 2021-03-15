class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        def func(n):
            if not n % 3 and not n % 5:
                return "FizzBuzz"
            if not n % 3:
                return "Fizz"
            if not n % 5:
                return "Buzz"
            return str(n)
        return [func(x) for x in range(1, n+1)]