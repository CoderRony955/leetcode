from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        return sum(nums) % k

obj = Solution()
print(obj.minOperations([3,9,7], 5))