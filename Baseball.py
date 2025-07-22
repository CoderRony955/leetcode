from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if not isinstance(operations, list):
            raise TypeError('operations must be a valid list object')
        
        if len(operations) == 0:
            return None
        
        record = []
        for i in operations:
            if i.lstrip('-').isdigit():
                record.append(int(i))
            elif i == 'C':
                record.pop()
            elif i == 'D':
                record.append(2*record[-1])
            elif i == '+':
                record.append(record[-1] + record[-2])
        
        total = 0
        for j in record:
            total += j
        
        return total
    
obj = Solution()
print(obj.calPoints(["5","2","C","D","+"]))
print(obj.calPoints(["1","C"]))
print(obj.calPoints(["5","-2","4","C","D","9","+","+"]))
                
                