class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not isinstance(s, str):
            raise TypeError('s must be str object type')
        
        if not str:
            return None
        
        chars = list(s.lower())
        count = 0
        for char in range(len(chars) - 1):
            if chars[char] != chars[char + 1]:
                count += 1
        
        return count


obj = Solution()
print(obj.countKeyChanges('aAbBcC'))