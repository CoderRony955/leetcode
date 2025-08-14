class Solution:
    def maxDepth(self, s: str) -> int:
        left = right = 0
        ans = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
            ans = max(ans, left - right)
        
        return ans

obj = Solution()
print(obj.maxDepth("(1+(2*3)+((8)/4))+1"))