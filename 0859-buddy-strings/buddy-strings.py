import sys

class Solution:
    '''
    Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
    '''
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        # first check if the string are a close enough match:
        differingIndices = []
        for index, charFromA in enumerate(A):
            charFromB = B[index]
            if charFromA != charFromB:
                if len(differingIndices) == 2:
                    # Too much difference in strings
                    return False
                differingIndices.append(index)
        if len(differingIndices) == 1:
            return False

        if len(differingIndices) == 2:
            return A[differingIndices[0]] == B[differingIndices[1]] and A[differingIndices[1]] == B[differingIndices[0]]

        # identical strings, are there any duplicate letters we can switch around?
        charDict = {}
        for char in A:
            if char in charDict:
                return True
            charDict[char] = 'Exists'

        return False



pairsToTest = [
    # True
    {
        'A': 'aaaaaaaaaa',
        'B': 'aaaaaaaaaa',
    },
    # True
    {
        'A': 'aaaaaaaaab',
        'B': 'baaaaaaaaa',
    },
    # False
    {
        'A': 'aaaaaaaaaa',
        'B': 'aaaaaaaaaaa',
    },
    # False
    {
        'A': 'aaaaaaaaaab',
        'B': 'aaaaaaaaaaa',
    },
    # True
    {
        'A': 'aa',
        'B': 'aa',
    },
    # True
    {
        'A': 'ab',
        'B': 'ba',
    },
    # False
    {
        'A': 'ab',
        'B': 'ab',
    },
    # False
    {
        'A': 'abcd',
        'B': 'badc',
    },
    # False
    {
        'A': '',
        'B': '',
    },
    # False
    {
        'A': 'qwertyuiopasdfghjklzxcvbnm',
        'B': 'qwertyuiopasdfghjklzxcvbnm',
    },
    # True
    {
        'A': 'qwertyuiopasdfghjklzxcvbnmq',
        'B': 'qwertyuiopasdfghjklzxcvbnmq',
    },
]

solver = Solution()

for pair in pairsToTest:
    print(solver.buddyStrings(pair['A'], pair['B']))