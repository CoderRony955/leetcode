from typing import List 

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        if not isinstance(hours, list) or not isinstance(target, int):
            raise TypeError('hours must be a valid list object and target must be valid int object')

        for elements in hours:
            if not isinstance(elements, int):
                raise TypeError('list elements must be valid int object type')
        
        if not hours or not target:
            return None
        
        count = 0
        for targets in range(len(hours)):
            if hours[targets] >= target:
                count += 1
        
        return count
    

obj = Solution()
print(obj.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(obj.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))