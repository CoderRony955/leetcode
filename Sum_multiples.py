class Solution:
    def sumOfMultiples(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError('n must be a valid int type')

        if n <= 0:
            return None

        nums = []

        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                nums.append(i)

        return sum(nums)


obj = Solution()
print(obj.sumOfMultiples(7))
print(obj.sumOfMultiples(10))
print(obj.sumOfMultiples(9))
