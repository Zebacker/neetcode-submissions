class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: fresh += 1
                elif grid[r][c] == 2: queue.append((r, c))
        if fresh == 0: return 0
        while queue and fresh > 0:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
