import sys
from typing import List, Optional

class Solution:
    '''
    Given an array with n integers,
    check if it could become non-decreasing by modifying at most 1 element
    '''
    def __init__(self):
        self.foundDecrease = False
        self.twoAgo = None
        self.lastNumber = None

    def checkPossibility(self, nums: List[int]) -> bool:
        lastNumberStore = None
        for currentNumber in nums:
            self.twoAgo = self.lastNumber
            self.lastNumber = lastNumberStore
            lastNumberStore = currentNumber

            if self.lastNumber == None:
                continue
            if currentNumber >= self.lastNumber:
                continue

            if self.twoAgo != None and self.twoAgo > currentNumber and self.twoAgo < self.lastNumber:
                # No way to correct course
                return False
            if not self.foundDecrease:
                self.setFoundDecrease(True)
                continue
            # Found a decreasing number before; it is truly hopeless.
            return False
        return True

    def getLastNumber(self) -> Optional[int]:
        return self._lastNumber

    def setLastNumber(self, x: Optional[int]) -> None:
        self._lastNumber = x

    lastNumber = property(
        getLastNumber,
        setLastNumber,
        None,
        'The number prior to the last one from the List being evaluated.',
    )

    def getTwoAgo(self) -> Optional[int]:
        return self._twoAgo

    def setTwoAgo(self, x: Optional[int]) -> None:
        self._twoAgo = x

    twoAgo = property(
        getTwoAgo,
        setTwoAgo,
        None,
        'The number prior to the last one from the List being evaluated.',
    )

    def getFoundDecrease(self) -> bool:
        return self._foundDecrease

    def setFoundDecrease(self, foundDecrease: bool) -> None:
        self._foundDecrease = foundDecrease

    foundDecrease = property(
        getFoundDecrease,
        setFoundDecrease,
        None,
        'Either True or False depending on if a decreasing number has already been discovered in a position previous to the current one',
    )

solver = Solution()


# defaultInput = [2,3,3,2,4]
defaultInput = [3, 3, 2, 2]
inputArgs = sys.argv[1:]
numbersToTest = defaultInput
if len(inputArgs) >= 1:
    numbersToTest = [ int(x) for x in inputArgs ]

print(solver.checkPossibility(numbersToTest))