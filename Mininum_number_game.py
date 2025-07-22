from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        if not isinstance(nums, list):
            raise TypeError(
                'nums must be a valid list object that must contains int type elements')

        if len(nums) == 2:
            nums.reverse()
            return nums

        nums.sort()
        arr = []

        while nums:
            alice = nums.pop(0)
            bob = nums.pop(0)
            arr.append(bob)
            arr.append(alice)

        return arr


obj = Solution()
print(obj.numberGame([3, 2, 5, 4]))
print(obj.numberGame([2, 5]))
print(obj.numberGame([2, 7, 9, 6, 4, 6]))
