class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.visit_island(grid, i, j)
                    islands += 1
        return islands
    
    def visit_island(self, grid, i, j):
        if (i < 0 or i >= len(grid) or 
            j < 0 or j >= len(grid[0]) or 
            grid[i][j] != '1'):
            return
        
        grid[i][j] = '0'
        
        self.visit_island(grid, i+1, j)  # 위
        self.visit_island(grid, i-1, j)  # 아래
        self.visit_island(grid, i, j+1)  # 오른쪽
        self.visit_island(grid, i, j-1)  # 왼쪽
        