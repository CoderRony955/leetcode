class Solution:
    def smallestNumber(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError('n must be a valid int object')

        binary = bin(n)[2:]
        digit = 0

        if not '0' in binary:
            return n

        next_num = n
        
        for _ in range(n, 5000):
            next_num += 1
            if '0' in bin(next_num)[2:]:
                continue
            if not '0' in bin(next_num)[2:]:
                digit = next_num
                break

        return digit
