class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping1 = {}
        mapping2 = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in mapping1:
                if mapping1[char_s] != char_t:
                    return False
            else:
                mapping1[char_s] = char_t
            
            if char_t in mapping2:
                if mapping2[char_t] != char_s:
                    return False
            else:
                mapping2[char_t] = char_s
            
        
        return True
    
obj = Solution()
print(obj.isIsomorphic("egg", "add"))
print(obj.isIsomorphic("foo", "bar"))
print(obj.isIsomorphic("paper", "title"))
            