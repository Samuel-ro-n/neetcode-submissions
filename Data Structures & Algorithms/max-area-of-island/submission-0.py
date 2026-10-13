class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        visited= set()
        count= 0
        area= 0
        def dfs(r, c):
            nonlocal count, area
            if ( r<0 or c< 0 or r >= rows or c >= cols or grid[r][c]==0 or (r, c) in visited):
                return 
            else:
                visited.add((r,c))
                count+=1
                area= max(count, area)
            res= (dfs(r+1, c) or 
                  dfs(r-1, c) or 
                  dfs(r, c+1) or 
                  dfs(r, c-1))
        for i in range(rows):
            for j in range(cols):
                count=0
                dfs(i, j)
        return area
                