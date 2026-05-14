class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        I = 2147483647
        q = deque()

        # Step 1: add all treasure chest
        for i in range(n):
            for j in range(m):

                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        
        # Step 2: BFS
        while q:

            # size = len(q)

            # for _ in range(size):

            x, y = q.popleft()

            for dx, dy in directions:

                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == I:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))
