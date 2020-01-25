from typing import List

LAND = '1'
WATER = '0'

def overlaps(min1, max1, min2, max2):
    overlap = max(0, min(max1, max2) - max(min1, min2))
    if overlap > 0:
        return True
    if min1 == min2 or min1 == max2 or max1 == min2 or max1 == max2:
        return True
    if (min1 > min2 and max1 < max2) or (min2 > min1 and max2 < max1):
        return True
    return False

print(overlaps(0, 2, 1, 1))

# Definition for a Bucket.
class Bucket:
    def __init__(self, identifiers: List[int]):
        self.destination = None
        self.identifiers = set(identifiers)
    
    def hasDestination(self) -> bool:
        return self.destination != None

    def getDestination(self):
        if not self.hasDestination():
            return self
        return self.destination.getDestination()

    def combine(self, bucket):
        otherDestination = bucket.getDestination()
        thisDestination = self.getDestination()
        uniqueIdentifiers = otherDestination.identifiers | thisDestination.identifiers
        newBucket = Bucket(uniqueIdentifiers)
        otherDestination.destination = newBucket
        thisDestination.destination = newBucket

        return newBucket

    def contains(self, identifier: int) -> bool:
        return identifier in self.getDestination().identifiers

class Solution:
    '''
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.

    
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        
        nextRowIsland = 1
        rowIslands = {}
        currentRowIslandStart = None
        '''
        Here we are generating row islands that we will then be pairing with adjacent row islands to form
        groups that we will then combine into the true islands that are needed to get the correct answer
        '''
        for rowIndex, row in enumerate(grid):
            lastSpot = WATER
            lengthOfRow = len(row)
            rowIslands[rowIndex] = []
            for spotIndex, spot in enumerate(row):
                if lastSpot == WATER and spot == LAND:
                    currentRowIslandStart = spotIndex

                if spotIndex + 1 >= lengthOfRow and spot == LAND:
                    rowIslands[rowIndex].append((nextRowIsland, currentRowIslandStart, spotIndex))
                    nextRowIsland += 1
                    currentRowIslandStart = None
                elif spot == WATER and currentRowIslandStart != None:
                    rowIslands[rowIndex].append((nextRowIsland, currentRowIslandStart, spotIndex - 1))
                    nextRowIsland += 1

                if spot == WATER:
                    currentRowIslandStart = None
                
                lastSpot = spot

        nextGroup = 1
        maxRowIndex = len(grid)
        rowIslandsToGroups = {}
        for rowNumber in [rowNumber for rowNumber in range(maxRowIndex)]:
            for rowIslandNumber, startIndex, endIndex in rowIslands[rowNumber]:
                rowIslandsToGroups[rowIslandNumber] = []
                if rowNumber == 0:
                    rowIslandsToGroups[rowIslandNumber].append(nextGroup)
                    nextGroup += 1
                    continue
                for prevRowIslandNumber, prevStartIndex, prevEndIndex in rowIslands[rowNumber - 1]:
                    if overlaps(prevStartIndex, prevEndIndex, startIndex, endIndex):
                        for groupNumber in rowIslandsToGroups[prevRowIslandNumber]:
                            rowIslandsToGroups[rowIslandNumber].append(groupNumber)
                if len(rowIslandsToGroups[rowIslandNumber]) == 0:
                    rowIslandsToGroups[rowIslandNumber].append(nextGroup)
                    nextGroup += 1

        groupBuckets = {}
        allBuckets = []
        for rowIslandNumber in range(1, nextRowIsland):
            relatedGroups = rowIslandsToGroups[rowIslandNumber]
            for group in relatedGroups:
                if (groupBuckets.get(group, None)) == None:
                    newGroupBucket = Bucket([group])
                    groupBuckets[group] = newGroupBucket
                    allBuckets.append(newGroupBucket)
            relatedBuckets = [groupBuckets[group] for group in relatedGroups]
            firstBucket = relatedBuckets[0]
            for group in relatedGroups:
                if not firstBucket.contains(group):
                    newCombinedBucket = firstBucket.combine(groupBuckets[group])
                    allBuckets.append(newCombinedBucket)

        return len([resultBucket for resultBucket in allBuckets if not resultBucket.hasDestination()])
        
        
solver = Solution()

# 1
# inputGrid = [
#     '11110',
#     '11010',
#     '11000',
#     '00000',
# ]

# 3
# inputGrid = [
#     '11000',
#     '11000',
#     '00100',
#     '00011',
# ]

# 1
# inputGrid = [
#     '11011',
#     '10001',
#     '10001',
#     '11111',
# ]

# 5
# inputGrid = [
#     '101',
#     '010',
#     '101',
# ]

# 1
inputGrid = [
    '111',
    '010',
    '010',
]

print(solver.numIslands(inputGrid))