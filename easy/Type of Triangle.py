from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if not nums:
            return None

        a, b, c = nums

        if all(x == nums[0] for x in nums):
            return 'equilateral'

        elif a + b <= c or a + c <= b or b + c <= a:
            return 'none'
        elif a == b or a == c or b == c:
            return 'isosceles'

        return 'scalene'


obj = Solution()
print(obj.triangleType([3, 3, 3]))
print(obj.triangleType([3, 4, 5]))
print(obj.triangleType([3, 4, 3]))
