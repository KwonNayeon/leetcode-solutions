class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_r >= rows or
                    new_c < 0 or new_c >= cols or
                    (new_r, new_c) in visited):
                    continue
                if heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        return list(pacific & atlantic)