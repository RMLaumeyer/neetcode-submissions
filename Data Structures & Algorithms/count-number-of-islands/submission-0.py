class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):

            if min(r, c) < 0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c] == "0":
                return

            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1

        return count


            