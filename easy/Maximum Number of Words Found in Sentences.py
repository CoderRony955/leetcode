from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        if not isinstance(sentences, list):
            raise TypeError('sentence must be a valid list object')

        for elements in sentences:
            if not isinstance(elements, str):
                raise TypeError('elements should be a str object type')
            
        count = []
        for words in range(len(sentences)):
            count.append(len(sentences[words].split()))
        
        return max(count)
    

obj = Solution()
print(obj.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))