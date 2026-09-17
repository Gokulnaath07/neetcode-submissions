class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #n no of nodes and i have given edges [ai, bi]

        adj=[[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=set()
        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        component=0
        for i in range(n):
            if i not in visited:
                component+=1
                dfs(i)
        return component

        