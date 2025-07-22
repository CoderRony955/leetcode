class Solution:
    def countDigits(self, num: int) -> int:
        if not isinstance(num, int):
            raise TypeError('num must be valid int object')
        
        if num == 0:
            return 0
        
        conv = str(num)
        l = [int(i) for i in conv]
        count = 0
        
        for j in l:
            if num % j == 0:
                count += 1
        
        return count
    
obj = Solution()
print(obj.countDigits(1248))
print(obj.countDigits(121))
print(obj.countDigits(7))
        
    