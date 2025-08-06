class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        to_str = str(x)
        sum_of = [int(i) for i in to_str]
        if x % sum(sum_of) == 0:
            return sum(sum_of)
        return -1
        
    
obj = Solution()
print(obj.sumOfTheDigitsOfHarshadNumber(18))