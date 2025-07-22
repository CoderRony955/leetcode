class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        if not isinstance(num, int) or not isinstance(t, int):
            raise TypeError('both given parameters must be a valid integer')
        x = num + 2 * t
        return x 

obj = Solution()
print(obj.theMaximumAchievableX(4, 1))