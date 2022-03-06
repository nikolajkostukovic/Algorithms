
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self,root) :
        ans = []
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            ans.append(node.val)
        if not root:
            return ans
        helper(root)
        return ans