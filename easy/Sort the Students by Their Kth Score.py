from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)

obj = Solution()
print(obj.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))
print(obj.sortTheStudents([[3,4],[5,6]], 0))