# Vertical order traversal of Binary tree 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque([(root,0,0)]) #node , col
        min_col, max_col = 0, 0
        cols = defaultdict(list) #col index -> list of values 

        while q:
            node, row, col = q.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            cols[col].append((row, node.val))

            if node.left:
                q.append((node.left, row+1, col-1))
            if node.right:
                q.append((node.right, row+1, col+1))
        result = []
        for c in range(min_col, max_col + 1):
            cols[c].sort()
            result.append([val for r, val in cols[c]])
        return result
        
# Max width of a Binary Tree 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root, 1, 0]]) #[node, num, level]
        prevLevel, prevNum = 0, 1

        while q:
            node, num, level = q.popleft()
            if level > prevLevel:
                prevLevel = level
                prevNum = num
            res = max(res, num -prevNum + 1)
            if node.left:
                q.append([node.left, 2*num, level + 1])
            if node.right:
                q.append([node.right, 2*num + 1, level + 1])
        return res