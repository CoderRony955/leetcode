class Solution:
    def convertDateToBinary(self, date: str) -> str:
        if not isinstance(date, str):
            raise TypeError('data must be a str object')
        
        l = date.split('-')
        binary = []
        for i in l:
            binary.append(bin(int(i))[2:])

        return '-'.join(binary)        