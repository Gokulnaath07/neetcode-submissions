class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #create a graph map with set and a indegree map
        #build the relationship and map the indegree values
        #bfs

        graph=defaultdict(set)

        for word in words:
            for char in word:
                if char not in graph:
                    graph[char]=set()
        indegree={char: 0 for char in graph}

        for i in range(1, len(words)):
            word1=words[i-1]
            word2=words[i]
            wordDiff=False
            for j in range(min(len(word1), len(word2))):
                if word1[j]!=word2[j]:
                    wordDiff=True
                    graph[word1[j]].add(word2[j])
                    break
            if not wordDiff and len(word2)<len(word1):
                return ""
        
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        queue=deque()
        for node in indegree:
            if indegree[node]==0:
                queue.append(node)
        res=[]
        while queue:
            char=queue.popleft()
            res.append(char)

            for neighbor in graph[char]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)

        if len(res)!=len(graph):
            return ""

        return "".join(res) 




        

        