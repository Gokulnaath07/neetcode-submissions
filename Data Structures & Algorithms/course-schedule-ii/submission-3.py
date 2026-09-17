class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        adj=[[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
        path=set()
        visited=set()
        res=[]
        def dfs(course):

            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]


        