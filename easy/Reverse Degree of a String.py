class Solution:
    def reverseDegree(self, s: str) -> int:
        letters = {
            'a': 26, 'b': 25, 'c': 24, 'd': 23, 'e': 22, 'f': 21,
            'g': 20, 'h': 19, 'i': 18, 'j': 17, 'k': 16, 'l': 15,
            'm': 14, 'n': 13, 'o': 12, 'p': 11, 'q': 10, 'r': 9,
            's': 8, 't': 7, 'u': 6, 'v': 5, 'w': 4, 'x': 3, 'y': 2,
            'z': 1
        }

        l = []
        inc = 1
        for key, val in letters.items():
            for index, char in enumerate(s, start=1):
                if key == char:
                    l.append(val * index)
                    inc += 1
        
        return sum(l)

obj = Solution()
print(obj.reverseDegree('abc'))
print(obj.reverseDegree('zaza'))
