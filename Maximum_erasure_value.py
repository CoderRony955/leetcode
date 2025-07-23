from typing import List
from collections import defaultdict

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not isinstance(nums, list):
            raise TypeError('nums must be a valid list object')
        
        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('elements should be an int object type')

        counter = defaultdict(int)
        count = 0 
        value = 0
        j = 0
        
        for i in range(len(nums)):
            count += nums[i]
            counter[nums[i]] += 1
            
            while counter[nums[i]] > 1:
                counter[nums[j]] -= 1
                count -= nums[j]
                j += 1
        
            value = max(value, count)
        
        return value
                
                
            
    
obj = Solution()
print(obj.maximumUniqueSubarray([4,2,4,5,6]))
print(obj.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
print(obj.maximumUniqueSubarray([187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965, 429, 166, 809, 340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367, 490, 787, 670, 476, 278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]
))