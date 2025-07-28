class Solution:
    def findComplement(self, num: int) -> int:
        if not num:
            return None
        
        l = list(bin(num)[2:])
        flip = []
        
        for digit in range(len(l)):
            if l[digit] == '1':
                flip.append('0')
            elif l[digit] == '0':
                flip.append('1')
        
        binaray_res = ''.join(flip)
        return int(binaray_res, 2)


obj = Solution()
print(obj.findComplement(5))
print(obj.findComplement(1))
print(obj.findComplement(1073741824))