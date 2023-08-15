# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = []
        right = []

        if head is None:
            return None

        curr_node = head
        while curr_node is not None:
            curr_val = curr_node.val
            if curr_val < x:
                left.append(curr_val)
            else:
                right.append(curr_val)
            curr_node = curr_node.next

        list_input = left + right
        list_with_nodes = []
        for pos, val in enumerate(list_input[::-1]):
            if pos == 0:
                list_with_nodes.append(ListNode(val))
            else:
                list_with_nodes.append(ListNode(val, list_with_nodes[-1]))

        return list_with_nodes[::-1][0]



s = Solution()
print("Example 1: ")
list_input = [1, 4, 3, 2, 5, 2]
list_with_nodes = []
for pos, val in enumerate(list_input[::-1]):
    if pos == 0:
        list_with_nodes.append(ListNode(val))
    else:
        list_with_nodes.append(ListNode(val, list_with_nodes[-1]))
list_with_nodes = list_with_nodes[::-1]
print(s.partition(list_with_nodes[0], 3))  # [1,2,2,4,3,5]

print("Example 2: ")
list_input = [2, 1]
list_with_nodes = []
for pos, val in enumerate(list_input[::-1]):
    if pos == 0:
        list_with_nodes.append(ListNode(val))
    else:
        list_with_nodes.append(ListNode(val, list_with_nodes[-1]))
list_with_nodes = list_with_nodes[::-1]
print(s.partition(list_with_nodes[0], 2))  # [1,2]

print("Example 3: ")
list_input = []
list_with_nodes = []
for pos, val in enumerate(list_input[::-1]):
    if pos == 0:
        list_with_nodes.append(ListNode(val))
    else:
        list_with_nodes.append(ListNode(val, list_with_nodes[-1]))
list_with_nodes = list_with_nodes[::-1]
print(s.partition(None, 2))  # [1,2]
