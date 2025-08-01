class Solution:
    def interpret(self, command: str) -> str:
        if not command:
            return None
        
        newstr = command.replace('()', 'o')
        newstr2 =  newstr.replace('(', '')
        return newstr2.replace(')', '')

obj = Solution()
print(obj.interpret("G()(al)"))
print(obj.interpret("G()()()()(al)"))