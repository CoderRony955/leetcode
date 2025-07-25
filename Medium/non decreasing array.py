from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not isinstance(nums, list):
            raise TypeError('nums must be list object')

        for elements in nums:
            if not isinstance(elements, int):
                raise TypeError('nums elements must be a int object type')
        
        if not nums:
            return None
        
        if len(nums) == 1:
            return True

        l = [num for num in nums]
        count = 0
        
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                count += 1
                
                if count > 1:
                    return False
                
                elif i == 0 or l[i - 1] <= l[i + 1]:
                    l[i] = l[i + 1]
                else:
                    l[i + 1] = l[i]
            
            elif l == sorted(l):
                return True
        
        return True
        

obj = Solution()
print(obj.checkPossibility([4,2,3]))    
print(obj.checkPossibility([4, 2, 1]))    
print(obj.checkPossibility([-1,4,2,3]))    
            
            
                