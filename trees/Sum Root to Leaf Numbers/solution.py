from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(node, current):
            if not node:
                return 0
            current = (current * 10) + node.val
            if not node.left and not node.right:
                return current
            left = solve(node.left, current)
            right = solve(node.right, current)
            return left + right
        return solve(root, 0)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print(solution.sumNumbers(root))