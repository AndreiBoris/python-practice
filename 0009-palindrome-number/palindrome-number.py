import sys

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

solver = Solution()

defaultInput = [101, 102, 1, 100000000000000000000000000000001, 12, 111, -111, 1]
inputArgs = sys.argv[1:]
numbersToTest = defaultInput
if len(inputArgs) >= 1:
    numbersToTest = [ int(x) for x in inputArgs ]

for x in numbersToTest:
    print(solver.isPalindrome(x))