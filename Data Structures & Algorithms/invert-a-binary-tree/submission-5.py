# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        # def dfs(root):

        #     if not root:
        #         return None

            
        #     temp=root.left
        #     root.left=root.right
        #     root.right=temp

        #     left=dfs(root.left)
        #     right=dfs(root.right)

        #     return root
        # return dfs(root)

        #BFS
        res=[]
        if not root:
            return None
        
        queue=deque([root])

        while queue:
            node=queue.popleft()

            node.left, node.right=node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root








