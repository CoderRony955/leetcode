from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ ans[i])
        return ans
    
obj = Solution()
print(obj.decode([1,2,3], 1))

