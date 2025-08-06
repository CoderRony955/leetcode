class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        l1 = []
        idx = word.index(ch)
        
        for char in word[:idx+1]:
            l1.append(char)
        l1.reverse()
        
        l2 = []
        for char2 in word[idx+1:]:
            l2.append(char2)
            
        merge = l1 + l2
        return ''.join(merge)
    
obj = Solution()
print(obj.reversePrefix("abcdefd", "d"))