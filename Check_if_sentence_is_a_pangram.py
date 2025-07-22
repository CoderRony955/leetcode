class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if not isinstance(sentence, str):
            raise TypeError('sentence must be a valid str object')
        
        alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
        
        if len(set(sentence)) >= len(alphabet_set):
            return True
        
        return False
    
    
obj = Solution()
print(obj.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
print(obj.checkIfPangram('leetcode'))

# 2nd solution ---------------------------------------------------


# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         if not isinstance(sentence, str):
#             raise TypeError('sentence must be a valid str object')
        
#         alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
        
#         i = 0
#         has = []
    
#         while i < len(sentence):
#             if alphabet_set.issubset(sentence):
#                 has.append(True)
#             i += 1
        
#         if len(has) >= len(alphabet_set):
#             return True
        
#         return False