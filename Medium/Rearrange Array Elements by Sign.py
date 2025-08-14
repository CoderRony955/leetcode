from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = [i for i in nums if i < 1]
        pos = [j for j in nums if j >= 1]
        ans = []
        for k, m in zip(neg, pos):
            ans.append(m)
            ans.append(k)
        return ans

obj = Solution()
print(obj.rearrangeArray([3,1,-2,-5,2,-4]))

        