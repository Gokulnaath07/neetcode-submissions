# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # if not root: return None

        # temp=root.right
        # root.right=root.left
        # root.left=temp

        # self.invertTree(root.right)
        # self.invertTree(root.left)

        # return root

        #BFS
        if not root:
            return None
        
        queue=deque([root])

        res=[]

        while queue:
            
            node=queue.popleft()
            temp=node.right
            node.right=node.left
            node.left=temp

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

        