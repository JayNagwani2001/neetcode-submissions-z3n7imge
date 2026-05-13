class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        vis = [[0]*m for _ in range(n)]

        def dfs(i, j, s):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 
            vis[i][j] = 1
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m or (nx, ny) in s:
                    continue
                else:
                    # print([nx, nx])
                    if heights[i][j] <= heights[nx][ny]:
                        s.append((nx, ny))
                        dfs(nx, ny, s)


        p = list()
        for i in range(n):
            p.append((i, 0))
        for j in range(m):
            p.append((0, j))

        for x, y in p:
            dfs(x, y, p)

        a = list()
        for i in range(n):
            a.append((i, m-1))
        for j in range(m):
            a.append((n-1, j))

        for x, y in a:
            dfs(x, y, a)

        ans = list(set(p).intersection(set(a)))

        return ans

