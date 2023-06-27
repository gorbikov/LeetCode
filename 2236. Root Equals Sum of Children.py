# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


s = Solution()
print("Example 1: ")
left = TreeNode(4)
right = TreeNode(6)
root = TreeNode(10, left, right)
print(s.checkTree(root))
print("Example 2: ")
left = TreeNode(3)
right = TreeNode(1)
root = TreeNode(5, left, right)
print(s.checkTree(root))
