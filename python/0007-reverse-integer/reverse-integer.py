import sys
# max is  2147483647
# min is -2147483648

class Solution:
    '''
    Reverses an integer while maintaining sign. Does not store resulting integers that
    overflow signed 32 bit integer.
    '''

    def reverse(self, x: int) -> int:
        self.parseSign(x)
        absoluteX = abs(x)
        stringX = str(absoluteX)
        reversedX = stringX[::-1]

        reversedInt = int('%s%s' % (self.negativeSign, reversedX))

        if self.isOverflowing(reversedInt):
            return 0

        return reversedInt

    def parseSign(self, x: int) -> str:
        if x >= 0:
            self.negativeSign = ''
        else:
            self.negativeSign = '-'


    def isOverflowing(self, x: int) -> bool:
        if x > 2147483647:
            return True
        if x < -2147483648:
            return True
        return False

    def getNegativeSign(self) -> str:
        return self._negativeSign

    def setNegativeSign(self, sign: str) -> None:
        self._negativeSign = sign

    negativeSign = property(
        getNegativeSign,
        setNegativeSign,
        None,
        'Either "" or "-" depending on if the number is negative or not',
    )

solver = Solution()

defaultInput = [102, -102]
inputArgs = sys.argv[1:]
numbersToTest = defaultInput
if len(inputArgs) >= 1:
    numbersToTest = [ int(x) for x in inputArgs ]

for x in numbersToTest:
    print(solver.reverse(x))