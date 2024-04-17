from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf_DFS(self, root: Optional[TreeNode]) -> str:
        self.result = ''
        def solve(node, current):
            if not node:
                return ''
            current = chr(node.val + 97) + current
            if not node.left and not node.right:
                if self.result == '' or self.result > current:
                    self.result = current
                return
            solve(node.left, current)
            solve(node.right, current)
        solve(root, '')
        return self.result
    
    def smallestFromLeaf_BFS(self, root: Optional[TreeNode]) -> str:
        result = ''
        queue = [(root, chr(root.val + 97))]
        while queue:
            node, current = queue.pop(0)
            if not node.left and not node.right:
                if result == '' or result > current:
                    result = current
            if node.left:
                queue.append((node.left, chr(node.left.val + 97) + current))
            if node.right:
                queue.append((node.right, chr(node.right.val + 97) + current))
        return result

if __name__ == '__main__':
    # [0,1,2,3,4,3,4]
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    solution = Solution()
    print(f'Using BFS: {solution.smallestFromLeaf_BFS(root)}')
    print(f'Using DFS: {solution.smallestFromLeaf_DFS(root)}')