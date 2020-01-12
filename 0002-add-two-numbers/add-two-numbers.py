from typing import List
import math

# We are going to want to go through each of these and sum it with all other numbers with a later index to see if they
# add up, storing the indexes as we go

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return createListFromInt(createIntFromList(l1) + createIntFromList(l2))


def createIntFromList(node1: ListNode) -> int:
    numberString = '%s' % node1.val
    currentNode = node1;
    while currentNode.next is not None:
        currentNode = currentNode.next
        numberString = '%s%s' % (currentNode.val, numberString)

    return int(numberString)

def createListFromInt(num: int) -> ListNode:
    if num == 0:
        return ListNode(0)

    firstNode = None
    lastNode = None
    remainingNum = num
    while remainingNum > 0:
        smallestDigit = remainingNum % 10
        remainingNum = math.floor(remainingNum / 10)
        newNode = ListNode(smallestDigit)
        if lastNode is not None:
            lastNode.next = newNode
        if firstNode is None:
            firstNode = newNode
        lastNode = newNode

    return firstNode

# hold the number 321
listA1 = ListNode(1)
listA2 = ListNode(2)
listA3 = ListNode(3)
listA1.next = listA2
listA2.next = listA3

# hold the number 5050
listB1 = ListNode(0)
listB2 = ListNode(5)
listB3 = ListNode(0)
listB4 = ListNode(5)
listB1.next = listB2
listB2.next = listB3
listB3.next = listB4

solver = Solution();
solution = solver.addTwoNumbers(listA1, listB1);

print(createIntFromList(solution));