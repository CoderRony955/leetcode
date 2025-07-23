from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not isinstance(s, str):
            raise TypeError('s must be a str object type')
        
        if not s:
            return None
        
        char_count = Counter(s)
        
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1
    
obj = Solution()
print(obj.firstUniqChar('leetcode'))
print(obj.firstUniqChar('loveleetcode'))
print(obj.firstUniqChar('dddccdbba'))