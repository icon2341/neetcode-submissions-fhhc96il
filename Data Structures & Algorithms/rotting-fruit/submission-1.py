from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # given a 2d grid
        # each cell can have a 0 empty 1 fresh 2 rotten
        # every minute if a fresh fruit is horizontally or vertically adjacent to a rotten fruit
        # then the fresh fruit is ALSO Rotten

        # return minimum number of minutes that must elapse until there are zero fresh
        # remaining

        # intersting problem.
        
        COLS,ROWS = len(grid[0]), len(grid)

        visited = set()
        queue = deque()
        maxPath = float("-inf")
        fresh_fruit = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] != 2):
                    if(grid[i][j] == 1):
                        fresh_fruit += 1
                    continue
                queue.append((i,j))

        def addQueue(r,c):
            nonlocal fresh_fruit
            if(r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 2 or grid[r][c] == 0 or (r,c) in visited):
                return
            visited.add((r,c))
            queue.append((r,c))
            fresh_fruit -= 1
        
        distance = 0
        while(queue and fresh_fruit > 0):
            distance +=1
            for i in range(len(queue)):
                # for each item in the queue 
                r,c = queue.popleft()
                grid[r][c] == 2

                addQueue(r+1,c)
                addQueue(r-1,c)
                addQueue(r,c+1)
                addQueue(r,c-1)

        if(fresh_fruit > 0):
            return -1

        return distance


# was able to come out with the basic solution on my own
            


            

