# Max Path Sum 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        #return max path sum without split
        def dfs(root):
            if not root:return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax= max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
        
    
# BT form Preorder and Inorder Traversal 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # create sublist/ partition
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

# BT from post order and Inorder 
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v:i for i, v in enumerate(inorder)}

        def helper(l,r):

            if l > r:
                return None
        
            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]
            root.right = helper(idx+1,r)
            root.left = helper(l, idx-1)
            return root
        return helper(0, len(inorder)-1)
        