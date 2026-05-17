class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #order of seq of cources: topological sorting
        adj = defaultdict(list)
        indegree = [0]*numCourses
        for u, v in prerequisites:
            if u == v:
                return False
            indegree[u] += 1 
            adj[v].append(u)

        vis = [0]*numCourses
        toposort = []
        q = deque()

        for i, ind in enumerate(indegree):
            if ind == 0:
                q.append(i)
        
        print(indegree)
        while q:
            node = q.popleft()
            toposort.append(node)
            for ele in adj[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    q.append(ele)
            

        if len(toposort) != numCourses:
            return []
        
        return toposort