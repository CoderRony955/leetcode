from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_val = max(arr)
        return arr.index(max_val)

obj = Solution()
print(obj.peakIndexInMountainArray())