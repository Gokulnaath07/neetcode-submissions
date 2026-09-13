# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue=deque([root])
        res=[]
        count=1
        while queue:
            level=[0]*len(queue)
            if count%2==0:
                idx=-1
            else:
                idx=0

            for i in range(len(queue)):
                node=queue.popleft()
                left, right=node.left, node.right
                level[idx]=node.val
                if count%2==0:
                    idx-=1
                else:
                    idx+=1
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            count+=1
            res.append(level)
        return res
                
                


