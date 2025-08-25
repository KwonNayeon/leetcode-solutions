from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid), len(grid[0])
        
        islands = 0

        visited = [[False] * m for _ in range(n)]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def in_range(r, c):
            return 0 <= r < n and 0 <= c < m

        def passable(r, c):
            return grid[r][c] == "1"

        def bfs(r, c):
            q = deque([(r, c)])
            visited[r][c] = True

            while q:
                cur_r, cur_c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc
                    if in_range(nr, nc) and passable(nr, nc) and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and not visited[r][c]:
                    islands += 1
                    bfs(r, c)

        return islands
        