# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def set_val(self, x):
        self.val = x
    def set_next(self, l):
        self.next = l
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        prev_nodes = []
        curr_node = head
        while True:
            prev_nodes.append(curr_node)
            if curr_node.next is None:
                return False
            if curr_node.next in prev_nodes:
                return True
            curr_node = curr_node.next


s = Solution()
print("Example 1:")
h4 = ListNode(-4)
h3 = ListNode(0)
h3.set_next(h4)
h2 = ListNode(2)
h2.set_next(h3)
h4.set_next(h2)
h1 = ListNode(3)
h1.set_next(h2)
print(s.hasCycle(h1))

print("Example 2:")
h2 = ListNode(2)
h2.set_next(h3)
h1 = ListNode(1)
h2.set_next(h1)
h1.set_next(h2)
print(s.hasCycle(h1))

print("Example 3:")
h1 = ListNode(1)
print(s.hasCycle(h1))

print("Example 4:")
h1 = ListNode("")
print(s.hasCycle(h1))


