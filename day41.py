# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Constructing a BST from preorder traversals 

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        N = len(preorder)
        root = TreeNode(preorder[0])

        stack.append(root)
        for i in range(1,N):
            # if this value is less than the node of root , we add to the left 
            if preorder[i] < stack[-1].val:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            #add ,right pop off stack to know which one
            else:
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
        return root
    
# validate BST
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            if node.val <= left or node.val >= right:
                return False
                
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
                    
# LCA of BST

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur



