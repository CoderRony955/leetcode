from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        if not isinstance(nums, list):
            raise TypeError(
                'nums must be a valid list object that contains int object type elements')

        if len(nums) == 0:
            return 0

        double_digits = [n for n in nums if 10 <= n <= 99]
        rest = [n for n in nums if not (10 <= n <= 99)]

        Alice = sum(rest)
        Bob = sum(double_digits)

        Won = True

        if Alice == Bob:
            Won = False

        elif Alice > Bob:
            Won = True

        return Won


obj = Solution()
print(obj.canAliceWin([1, 2, 3, 4, 10]))
print(obj.canAliceWin([1, 2, 3, 4, 5, 14]))
print(obj.canAliceWin([5, 5, 5, 25]))
