from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if not nums:
            return None

        ans = []
        for i in range(0, len(nums), 2):
            req = nums[i]
            val = nums[i + 1]
            ans.extend([val] * req)

        return ans


obj = Solution()
print(obj.decompressRLElist([1, 2, 3, 4]))
