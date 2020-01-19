import sys
from typing import List

class Solution:
    '''
    Given a non-empty array of integers, return the third maximum number in this array. 
    If it does not exist, return the maximum number. The time complexity must be in O(n).
    '''
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = None
        secondMax = None
        thirdMax = None
        for num in nums:
            if num == firstMax or num == secondMax or num == thirdMax:
                continue
            if firstMax == None or num > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = num
                continue
            if secondMax == None or num > secondMax:
                thirdMax = secondMax
                secondMax = num
                continue
            if thirdMax == None or num > thirdMax:
                thirdMax = num
        
        if thirdMax == None:
            return firstMax
        return thirdMax

numsToTest = [
    # 1
    [3, 2, 1],
    # 2
    [1, 2],
    # 1
    [2, 2, 3, 1],
]

solver = Solution()

for nums in numsToTest:
    print(solver.thirdMax(nums))