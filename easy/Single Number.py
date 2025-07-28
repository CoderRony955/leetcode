from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        element = 0
        for key, val in count.items():
            if val == 1:
                element = key
        
        return element


obj = Solution()
print(obj.singleNumber([2,2,1]))
print(obj.singleNumber([4,1,2,1,2]))