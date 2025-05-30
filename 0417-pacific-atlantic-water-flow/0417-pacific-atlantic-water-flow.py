class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                new_r, new_c = r + dr, c + dc

                if (0 <= new_r < rows and
                    0 <= new_c < cols and
                    (new_r, new_c) not in visited and
                    heights[new_r][new_c] >= heights[r][c]):

                    dfs(new_r, new_c, visited)

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        return [[r, c] for r, c in pacific & atlantic]