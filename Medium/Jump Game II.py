from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return None

        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
        return jumps


obj = Solution()
print(obj.jump([2, 3, 1, 1, 4]))
print(obj.jump([2, 3, 0, 1, 4]))
