# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()

            path.append('R')
            if findPath(root.right, value, path):
                return True
            path.pop()
            return False
        
        s_path, d_path = [], []
        # find the path to both values respectively
        findPath(root, startValue, s_path)
        findPath(root, destValue, d_path)
        
        p = 0
        n_s, n_d = len(s_path), len(d_path)
        # Get rid of the longest common prefix for both paths
        while p < n_s and p < n_d and s_path[p] == d_path[p]:
            p += 1
        
        return 'U' * len(s_path[p:]) + ''.join(d_path[p:])
        

            


