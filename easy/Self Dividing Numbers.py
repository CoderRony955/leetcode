from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            if '0' in str(num):
                continue
            split = [int(i) for i in str(num)]
            if all(num % n == 0 for n in split):
                result.append(num)

        return result


obj = Solution()
print(obj.selfDividingNumbers(47, 85))
print(obj.selfDividingNumbers(1, 22))
