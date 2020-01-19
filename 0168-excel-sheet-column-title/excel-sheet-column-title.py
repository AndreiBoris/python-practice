import sys
import typing

# Right before A
CHAR_START_INDEX = 64 
BASE_VALUE = 26

class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''
        while n > 0:
            modulo = int(n % BASE_VALUE)
            if modulo == 0:
                # So we don't slip when it comes to catching 'Z'
                modulo = 26 
            title = '%s%s' % (chr(CHAR_START_INDEX + modulo), title)
            n = n - modulo
            n = n / BASE_VALUE
        return title

    

colNumsToTest = [
    # A
    1,
    # B
    2,
    # C
    3,
    # Z
    26,
    # AA
    27,
    # AB
    28,
    # MQ
    355,
    # ZY
    701,
    # AAA
    703,
    # DKI
    2999,
]   

solver = Solution()

for number in colNumsToTest:
    print(solver.convertToTitle(number))