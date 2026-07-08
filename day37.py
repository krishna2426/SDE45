#LCA in BT 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is null, or we found p or q
        if not root or root == p or root == q:
            return root
        
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right return a node, current root is the LCA
        if left and right:
            return root
            
        # Otherwise, return the non-null child (either left or right)
        return left if left else right
    
# same tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
# zig zag traversal 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root]if root else [])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = list(reversed(level)) if len(res) % 2 else level
            res.append(level)
        return 
    
#boundary level traversal

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isLeaf(self, root):
        """
        Function to check if a node is a leaf
        """
        return not root.left and not root.right

    def addLeftBoundary(self, root, res):
        """
        Function to add the left boundary of the tree
        """
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to the result
                res.append(curr.data)
            # Move to the left child if it exists,
            # otherwise move to the right child
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addRightBoundary(self, root, res):
        """
        Function to add the right boundary of the tree
        """
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                # If the current node is not a leaf,
                # add its value to a temporary vector
                temp.append(curr.data)
            # Move to the right child if it exists,
            # otherwise move to the left child
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        # Reverse and add the values from
        # the temporary vector to the result
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])

    def addLeaves(self, root, res):
        """
        Function to add the leaves of the tree
        """
        if self.isLeaf(root):
            # If the current node is a leaf,
            # add its value to the result
            res.append(root.data)
            return
        # Recursively add leaves of
        # the left and right subtrees
        if root.left:
            self.addLeaves(root.left, res)
        if root.right:
            self.addLeaves(root.right, res)

    def printBoundary(self, root):
        """
        Main function to perform the
        boundary traversal of the binary tree
        """
        res = []
        if not root:
            return res
        # If the root is not a leaf,
        # add its value to the result
        if not self.isLeaf(root):
            res.append(root.data)

        # Add the left boundary, leaves,
        # and right boundary in order
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)

        return res

