class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res=0
        left=0
        right=len(height)-1

        leftWall=height[left]
        rightWall=height[right]

        while left<right:
            if leftWall<rightWall:
                left+=1
                leftWall=max(leftWall, height[left])
                res+=leftWall-height[left]
            else:
                right-=1
                rightWall=max(rightWall, height[right])
                res+=rightWall-height[right]
        return res

        