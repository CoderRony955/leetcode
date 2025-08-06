class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        cur = num
        for _ in range(1, num+1):
            if cur % 2 == 0:
                cur = cur // 2
                count += 1
            elif cur % 2 != 0:
                cur = cur - 1
                count += 1
            if cur == 0:
                break

        return count


obj = Solution()
print(obj.numberOfSteps(14))
