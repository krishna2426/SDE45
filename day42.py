class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# floor in BST

def Soution():
    floor = -1
    while root:
        if root.data == key:
            floor = root.data
            return floor
        if key > root.data:
            floor = root.data
            root = root.right
        else:
            root = root.left 
    return floor

# ceil in BST
def Solution():
    ceil = -1
    while root:
        if root.data == key:
            ceil = root.data
            return ceil 
        if key > root.data:
            root = root.right
        else:
            ceil = root.data
            root = root.left
    return ceil


# kth smalllest element;
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n +=1
            if n == k:
                return curr.val
            curr = curr.right
