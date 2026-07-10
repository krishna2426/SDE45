# populating right pointer 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt  = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root
    
# bst from sorted array
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(l, r):
            if l > r : return None
            m = (l + r) // 2 #integer division 
            root = TreeNode(nums[m])       
            root.left = helper(l, m-1)
            root.right = helper(m+1,r)
            return root
        return helper(0,len(nums)-1)
    
# search in BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
        