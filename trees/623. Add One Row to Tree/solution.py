from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                temp_left = node.left
                temp_right = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = temp_left
                node.right.right = temp_right
                return
            add(node.left, current_depth+1)
            add(node.right, current_depth+1)
            return
            
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
            return root
        add(root, 1)
        return root

        