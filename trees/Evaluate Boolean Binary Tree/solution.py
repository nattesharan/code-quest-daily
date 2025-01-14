from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluate(node):
            if not node.left and not node.right:
                return bool(node.val)
            left = evaluate(node.left)
            right = evaluate(node.right)
            if node.val == 2:
                return left or right
            return left and right
        return evaluate(root)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    solution = Solution()
    print(solution.evaluateTree(root))
    
# Time complexity - O(n)
# Space complexity - O(1) in general and for recursion O(n)