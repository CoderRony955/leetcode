class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            F = self.fib(n - 1) + self.fib(n - 2)
        return F


obj = Solution()
print(obj.fib(4))
