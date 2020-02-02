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
        return self.checkCanBeNonDecreasing(nums, True)

    def checkCanBeNonDecreasing(self, nums: List[int], checkPossibility: bool = False) -> bool:
        lastNumberStore = None
        for index, currentNumber in enumerate(nums):
            lastNumber = lastNumberStore
            lastNumberStore = currentNumber

            if lastNumber == None:
                continue
            if currentNumber >= lastNumber:
                continue

            if checkPossibility:
                canDropLastNumber = self.checkCanBeNonDecreasing(
                    [number for innerIndex, number in enumerate(nums) if innerIndex != index - 1]
                )
                canDropCurrentNumber = self.checkCanBeNonDecreasing(
                    [number for innerIndex, number in enumerate(nums) if innerIndex != index]
                )
                if canDropLastNumber or canDropCurrentNumber:
                    continue

            return False

        return True

solver = Solution()


# defaultInput = [2,3,3,2,4]
defaultInput = [3, 3, 2, 2]
inputArgs = sys.argv[1:]
numbersToTest = defaultInput
if len(inputArgs) >= 1:
    numbersToTest = [ int(x) for x in inputArgs ]

print(solver.checkPossibility(numbersToTest))