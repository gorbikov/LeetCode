# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        string1 = str(l1.val)
        current_list_node = l1.next
        while current_list_node is not None:
            string1 = str(current_list_node.val) + string1
            current_list_node = current_list_node.next

        string2 = str(l2.val)
        current_list_node = l2.next
        while current_list_node is not None:
            string2 = str(current_list_node.val) + string2
            current_list_node = current_list_node.next

        string3 = str(int(string1) + int(string2))
        print(string3)

        for char in string3:
            current_list_node = ListNode(char, current_list_node)

        return current_list_node


s = Solution()
print("Example 1: ")
l1_3 = ListNode(3)
l1_2 = ListNode(4, l1_3)
l1_1 = ListNode(2, l1_2)
l2_3 = ListNode(4)
l2_2 = ListNode(6, l2_3)
l2_1 = ListNode(5, l2_2)
print(s.addTwoNumbers(l1_1, l2_1))
print("Example 2: ")
l1_1 = ListNode(0)
l2_1 = ListNode(0)
print(s.addTwoNumbers(l1_1, l2_1))
print("Example 3: ")
l1_7 = ListNode(9)
l1_6 = ListNode(9, l1_7)
l1_5 = ListNode(9, l1_6)
l1_4 = ListNode(9, l1_5)
l1_3 = ListNode(9, l1_4)
l1_2 = ListNode(9, l1_3)
l1_1 = ListNode(9, l1_2)
l2_4 = ListNode(9)
l2_3 = ListNode(9, l2_4)
l2_2 = ListNode(9, l2_3)
l2_1 = ListNode(9, l2_2)
print(s.addTwoNumbers(l1_1, l2_1))
