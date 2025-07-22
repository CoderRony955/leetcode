from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if not isinstance(words, list):
            raise TypeError(
                'words must be a valid list object that must contains int object type elements')

        if len(words) == 0:
            return 0

        palidromic = []

        for i in range(len(words)):
            if ''.join(reversed(words[i])) == words[i]:
                palidromic.append(words[i])
                break
            else:
                continue

        return ''.join(palidromic)


obj = Solution()
print(obj.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
print(obj.firstPalindrome(["notapalindrome", "racecar"]))
print(obj.firstPalindrome(["def", "ghi"]))
