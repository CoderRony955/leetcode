from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not isinstance(nums, list) or not isinstance(k, int):
            raise TypeError(
                'nums must be a valid list object and whereas k must be a valid int object')

        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('elements of nums must be a int object type')

        if not nums:
            return None

        n = len(nums)
        k %= n
    

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))
print(obj.rotate([-1,-100,3,99], 2))
               
        