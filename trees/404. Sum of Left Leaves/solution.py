from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
#         def solve(node, parent):
#             if not node:
#                 return 0
#             if not node.left and not node.right:
#                 if parent and parent.left == node:
#                     return node.val
#             left = solve(node.left, node)
#             right = solve(node.right, node)
#             return left + right
#         return solve(root, None)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solve(node: Optional[TreeNode], isLeft: bool):
            if not node:
                return 0
            if not node.left and not node.right and isLeft:
                return node.val
            left = solve(node.left, True)
            right = solve(node.right, False)
            return left + right
        return solve(root, False)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print(solution.sumOfLeftLeaves(root))
    
# Time complexity - O(n)
# Space complexity - O(1)