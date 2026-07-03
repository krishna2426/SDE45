class TreeNode:
    def __init__(self,val=0,right=None,left= None):
        self.val = val
        self.right = right
        self.left = left
        
class Solution:
    def inorderTraversal(self, root):
        arr = []
        self.inOrder(root,arr)
        return arr
    def inOrder(self, root, arr):
        if root is None:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)
        
    def preorderTraversal(self, root):
        arr = []
        self.preOrder(root, arr)
        return arr
    def preOrder(self, root, arr):
        if root is None:
            return
        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)
        
    def postorderTraversal(self,root):
        arr=[]
        self.postOrder(root, arr)
        return arr
    def postOrder(self, root, arr):
        if root is None:
            return
        self.postOrder(root.left, arr)
        self.postOrder(root.right, arr)
        arr.append(root.val)
    

if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()

    # Getting the postorder traversal
    result = sol.inorderTraversal(root)
    result1 = sol.preorderTraversal(root)
    result2 = sol.postorderTraversal(root)

    # Displaying the postorder traversal result
    print("In-order traversal:", result)
    print("Pre-order traversal:", result1)
    print("Post-order traversal:", result2)
    