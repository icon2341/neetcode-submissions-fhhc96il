from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        # Step 1: Add all treasures to the queue first
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        # Step 2: Expand outwards from treasures
        dist = 0
        while queue:
            # Process the current "layer" of the BFS
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Update the cell with the distance from a treasure
                grid[r][c] = dist

                # Check 4-directional neighbors
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    # Only visit if in bounds, it's land (2147483647), and not visited
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and grid[nr][nc] == 2147483647):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            dist += 1