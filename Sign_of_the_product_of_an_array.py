from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if not isinstance(nums, list):
            raise TypeError('nums must ve valid list object')

        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('elements should be int object type')
        
        if not nums:
            return None
        
        negative = 0
        positive = 0
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                return 0
            elif nums[i] < 0:
                negative += 1
            elif nums[i] > 0:
                positive += 1
        
            i += 1
        
        if negative % 2 != 0:
            return -1
        
        return 1

obj = Solution()
print(obj.arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(obj.arraySign([1,5,0,2,-3]))
print(obj.arraySign([-1,1,-1,1,-1]))