class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #b-a
        if not prerequisites:
            return True
        adj=[[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        visited=set()
        path=set()

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
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        

        