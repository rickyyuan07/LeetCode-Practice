# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Tree DP
        def dfs(root):
            # Return (max if not pick root, max if pick root)
            if not root:
                return (0, 0)
            
            lft = dfs(root.left)
            rgt = dfs(root.right)
            # Case 1: not pick root
            not_pick = max(lft) + max(rgt)
            # Case 2: pick root
            pick = lft[0] + rgt[0] + root.val
            return (not_pick, pick)
        
        return max(dfs(root))