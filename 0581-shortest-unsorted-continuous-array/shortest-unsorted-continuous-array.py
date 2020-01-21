import sys
from typing import List

class Solution:
    '''
    Given an integer array, 
    you need to find one continuous subarray that if you only sort this subarray in ascending order, 
    then the whole array will be sorted in ascending order, too.

    You need to find the shortest such subarray and output its length.
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        indexedNums = enumerate(nums)
        
        sortedTuples = sorted(indexedNums, key = lambda i: i[1])
        numberedTuples = []
        numberedIndex = 0
        for index, number in sortedTuples:
            numberedTuples.append((index, numberedIndex))
            numberedIndex += 1
        firstBadIndex = None
        lastBadIndex = None
        for actualIndex, orderedIndex in numberedTuples:
            if actualIndex != orderedIndex:
                if firstBadIndex == None or firstBadIndex > actualIndex:
                    firstBadIndex = actualIndex
                if lastBadIndex == None or lastBadIndex < actualIndex:
                    lastBadIndex = actualIndex
        
        if firstBadIndex == None:
            return 0

        return 1 + lastBadIndex - firstBadIndex

        
solver = Solution()

numsToTest = [
    # 5
    [2, 6, 4, 8, 10, 9, 15],
]

for nums in numsToTest:
    print(solver.findUnsortedSubarray(nums))