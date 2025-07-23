class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if not isinstance(n, int) or not isinstance(start, int):
            raise TypeError('both n and start must be a valid int object')
        
        if not n:
            return None
        
        nums = []
        xor = 0
        
        for i in range(0, n):
            nums.append(start + 2*i)
        
        for elements in nums:
            xor ^= elements
        
        return xor    
            
    
obj = Solution()
print(obj.xorOperation(5, 0))
print(obj.xorOperation(4, 3))