from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not isinstance(nums, list):
            raise TypeError('nums must be a list object')

        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('elements of nums must be valid int object')
        
        if not nums:
            return None
        
        elements_count = dict(Counter(nums))
        return max(elements_count, key=elements_count.get)
            
        
    
obj = Solution()
print(obj.majorityElement([3,2,3]))
print(obj.majorityElement([2,2,1,1,1,2,2]))