class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start^goal)[2:].count("1")

obj = Solution()
print(obj.minBitFlips(10, 7))