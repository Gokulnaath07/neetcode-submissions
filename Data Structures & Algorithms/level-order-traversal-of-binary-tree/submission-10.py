# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # if not root:
        #     return []
        # queue=deque([root])
        # res=[]

        # while queue:
        #     level=[]
        #     for i in range(len(queue)):
        #         node=queue.popleft()
        #         level.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(level)
        # return res


        res=[]

        def dfs(root, depth):
            if not root:
                return None
            if depth==len(res):
                res.append([])
            res[depth].append(root.val)
            left=dfs(root.left, depth+1)
            right=dfs(root.right, depth+1)
            
        dfs(root, 0)
        return res
            

                
        

        