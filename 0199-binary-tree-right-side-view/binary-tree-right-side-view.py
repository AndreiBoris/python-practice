import sys
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

'''
The will do dfs.

We will add to a stack with node + depth

We will store deepest depth recorded

Whenever a node with a new depth is found we will store it in a dictionary with key depth value val, the way 
the search will work we will always find the right-most node at each depth first and future nodes at that depth
will not update that value.

As we go to each node, we will store it's left-hand node, and then its right-hand node. This will be the way
by which we determine which node will be visited next. After visiting a single node, we will take the topmost 
value of the stack and repeat the process.

We will terminate the loop when stack is empty

To produce the return value we will loop through the range 0 -> deepest depth and take the values from the dict
'''
        
solver = Solution()

# for digits in listOfDigits:
#     print(solver.rightSideView(digits))