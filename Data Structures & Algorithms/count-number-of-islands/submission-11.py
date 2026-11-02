class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        Island = 0
        visited = set()
        def dfs(r, c):
            if c < 0 or r < 0 or r >= rows or c >= cols: return
            elif (r, c) in visited or grid[r][c] == '0': return
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    Island += 1
                    dfs(r, c)
        return Island


