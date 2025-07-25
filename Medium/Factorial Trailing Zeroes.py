class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        count  = 0
        while n >= 5:
            n /= 5
            count += 1
        
        return count
                
    
obj = Solution()
print(obj.trailingZeroes(5))
print(obj.trailingZeroes(7))