class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#level order traversal :

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen= len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:

                res.append(level)
        return res

#depth of Binary Tree (recursive)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
    
#iterative

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # The number of nodes at the current level
            level_size = len(queue)
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add the children of the current node to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # After processing the entire level, increment the depth
            depth += 1
            
        return depth
    
# diameter of BT
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #returns height:
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
    
#balanced BT
     def isBalanced(self, root: Optional[TreeNode]) -> bool:
            def dfs(root):
                if root is None:
                    return [True, 0]
                left, right = dfs(root.left), dfs(root.right)
                balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
                return [balance, 1 + max(left[1], right[1])]
            
            return dfs(root)[0]
