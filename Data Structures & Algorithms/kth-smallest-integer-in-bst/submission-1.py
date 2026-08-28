# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]

        

        # queue=deque()
        # if root:
        #     queue.append(root)
        
        # while queue:
        #     node=queue.popleft()
        #     if node.val:
        #         res.append(node.val)
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)

        # res.sort()
        # return res[k-1]


        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res[k-1]
                    
                    

                

        
        