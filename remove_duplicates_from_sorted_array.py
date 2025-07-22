from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not isinstance(nums, list):
            raise TypeError('nums must be a valid list object that must contains int object type elements')
        
        if len(nums) == 0:
            return 0 
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] == nums[right]:
                nums.remove(nums[left])
            
            right -= 1  
        
        return len(nums)
            
obj = Solution()
print(obj.removeDuplicates([1,1,2]))
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) 