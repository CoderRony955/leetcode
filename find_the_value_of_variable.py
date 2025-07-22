from typing import Any, List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        if not isinstance(operations, list):
            raise TypeError(
                'operations is must be a valid list that contains str type elements')

        x = 0

        for i in operations:
            if i in ('X++', '++X'):
                x += 1
            elif i in ('--X', 'X--'):
                x -= 1

        return x


obj = Solution()
print(obj.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
