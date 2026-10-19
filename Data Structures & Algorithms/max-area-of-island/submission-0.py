class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if 0 > r or r >= ROWS or 0 > c or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            count = 1

            
            count += dfs(r,c-1)
            count += dfs(r,c+1)
            count += dfs(r-1,c)
            count += dfs(r+1,c)

            return count
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_count = max(max_count,dfs(r,c))

        return max_count

        