class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]: 
                        dfs(nr, nc, visited)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows -1, c, atlantic)
        return list(atlantic.intersection(pacific))
        

