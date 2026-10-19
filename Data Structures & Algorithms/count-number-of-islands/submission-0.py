class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0
        visited = set()
        def dfs(r,c):
            #1. check if its within the grid:
            # within grid (0 <= r < ROWS) or (0 <= c < COLS)
            if 0 > r or r >= ROWS or 0 > c or c >= COLS:
                return
            
            #2. if its water:
            if grid[r][c] == "0":
                return
            
            #3. if its visited (check the coordinate):
            if (r,c) in visited:
                return #skip
            
            #4. new: mark as visited then explore:
            visited.add((r,c)) #add the coordinate

            #explore:
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island_count += 1
                    dfs(r,c)
            

        return island_count
