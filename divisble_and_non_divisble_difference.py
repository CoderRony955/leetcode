class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if not isinstance(n, int) or not isinstance(m , int):
            raise TypeError('given both parameters must be an valid int object')
        
        if n < 0 or m < 0:
            return None
        
        ln = [i for i in range(1, n+1) if i % m != 0]
        lm = [j for j in range(1, n+1) if j % m == 0]
        
        total_n = 0
        total_m = 0
        
        for i in ln:
            total_n += i
        
        for j in lm:
            total_m += j
            
        return total_n - total_m

obj = Solution()
print(obj.differenceOfSums(5, 6))
        