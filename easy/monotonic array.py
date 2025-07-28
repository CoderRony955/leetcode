from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums:
            return None

        increasing = True
        descreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                increasing = False
            elif nums[i] < nums[i + 1]:
                descreasing = False

        if increasing or descreasing:
            return True
        return False


obj = Solution()
print(obj.isMonotonic([1, 2, 2, 3]))
print(obj.isMonotonic([6, 5, 4, 4]))
print(obj.isMonotonic([1, 3, 2]))
