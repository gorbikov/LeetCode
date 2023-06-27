# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(0, None)


s = Solution()
print("Example 1: ")
print(s.addTwoNumbers([2, 4, 3], [5, 6, 4]))
print("Example 2: ")
print(s.addTwoNumbers([0], [0]))
print("Example 3: ")
print(s.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
