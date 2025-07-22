from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not isinstance(nums, list):
            raise TypeError(
                'nums must be a valid list object that must contains int object type elements')

        if len(nums) == 0:
            return 0

        nums.sort()
        ans = []

        for i in nums:
            ans.append(i**2)

        ans.sort()
        return ans

  
obj = Solution()
print(obj.sortedSquares([-4, -1, 0, 3, 10]))
print(obj.sortedSquares([-7, -3, 2, 3, 11]))
