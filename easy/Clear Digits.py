class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:  
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

                

obj = Solution()
print(obj.clearDigits("abc"))
print(obj.clearDigits("cb34"))