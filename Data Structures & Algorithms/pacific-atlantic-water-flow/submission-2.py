class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])

        directions=[(1,0), (0,1), (0,-1), (-1, 0)]

        atlantic, pacific= set(), set()

        def dfs(r, c, visited):
            #this is to track the respected points that flows in to the respected oceans 
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc= r+dr, c+dc

                if (0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited and heights[nr][nc]>=heights[r][c]):
                    dfs(nr, nc, visited)
        
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        
        return list(atlantic & pacific)



        