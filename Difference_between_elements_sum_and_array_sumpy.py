from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        if not isinstance(nums, list):
            raise TypeError('nums must be a valid list object')

        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('elements should be int object type')
        
        if not nums:
            return None
        
        sum1 = 0
        sum2 = 0
        
        for i in nums:
            sum1 += i

        l1 = [str(j) for j in nums]
        string = ''.join(l1)
        l2 = [int(k) for k in string]
        
        for m in l2:
            sum2 += m
        
        return sum1 - sum2

obj = Solution()
print(obj.differenceOfSum([1,15,6,3]))
print(obj.differenceOfSum([1,2,3,4]))