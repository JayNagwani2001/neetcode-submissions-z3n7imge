class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            if u == v:
                return False
            adj[v].append(u)
        print(adj)

        vis = [0]*numCourses
        pathVis = [0]*numCourses

        def dfs(v, par): #detect cycle
            vis[v] = 1
            pathVis[v] = 1
            # ans = False
            for ch in adj[v]:
                if not vis[ch]:
                    ans = dfs(ch, v)
                    if ans:
                        return ans
                elif pathVis[ch]:
                    return True
                    
            pathVis[v] = 0
                
            return False

        for c in range(numCourses):
            if not vis[c]:
                res = dfs(c, -1)
                if res:
                    return False #return False if cycle is detected
    
        return True

