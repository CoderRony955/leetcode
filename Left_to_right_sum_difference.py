from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if not isinstance(nums, list):
            raise TypeError(
                'nums must be a valif list object that must contains integer type elements')

        if len(nums) == 0:
            return 0

        left_sum = []
        right_sum = []

        cal = 0

        for i in range(len(nums)):
            left_sum.append(cal)
            cal += nums[i]

        cal2 = 0

        for j in nums[::-1]:
            right_sum.append(cal2)
            cal2 += j

        right_sum.reverse()

        anwser = []
        k = 0

        while k < len(nums):
            anwser.append(abs(left_sum[k] - right_sum[k]))
            k += 1

        return anwser


obj = Solution()
print(obj.leftRightDifference([10, 4, 8, 3]))
