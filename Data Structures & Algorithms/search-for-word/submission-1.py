class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])

        visited=set()

        directions=[(0,1), (1,0), (0,-1), (-1, 0)]
        
        def dfs(r, c, i):

            if not (0<=r<rows and 0<=c<cols):
                return False
            if (board[r][c]!= word[i] or (r, c) in visited):
                return False
            if i==len(word)-1:
                return True
            visited.add((r,c))
            
            for dr, dc in directions:
                nr, nc=r+dr, c+dc

                if (dfs(nr, nc, i+1)):
                    return True
            visited.remove((r,c))
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
            

        