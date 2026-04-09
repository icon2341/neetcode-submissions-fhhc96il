from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # Ok despite some bugs my solution was actually great over all, 
        # we do BFS from each land point which finds the shortest path to only tresure and overwritght it
        # The more optimal solution is to do do a simultaneous BFS from EACH treasure simultaneousy
        # this is faster because it means we traverse less space and dont reduntantly go over the same paths.

        # My initial solution was to simply start from each land point, do BFS to the nearest treasure
        # and if one is found then record that value in the grid at that land point
        # skipping water and treasure

        # ROWS = len(grid)
        # COLS = len(grid[0])
        # # traversal that will find nearest treasure
        # # doesnt need to be recursvie
        # def findTresure(coord):
        #     queue =[(coord[0],coord[1],0)]
        #     visited = set()

        #     while(queue):
        #         row,col,distance = queue.pop(0)

        #         # check if out of bounds or visited or water
        #         if(row < 0 or row == ROWS or col < 0 or col == COLS or (row,col) in visited or grid[row][col] == -1):
        #             continue
        #         else:
        #             visited.add((row,col))
                
        #         if(grid[row][col] == 0):
        #             return distance

        #         queue.append((row+1,col,distance+1))
        #         queue.append((row-1,col,distance+1))
        #         queue.append((row,col+1,distance+1))
        #         queue.append((row,col-1,distance+1))

        #     return 2147483647

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if(grid[i][j]==-1 or grid[i][j] == 0):
        #             continue
        #         grid[i][j] = findTresure((i,j))

        # for the optimial solution, we do kind of the same thing but we 
        # simultaneously do it from the same BFS
        ROWS,COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if(r< 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])

        # loop through and find all the treasure chests and queue them to start the simul
        # BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        # distance tracker for ALL BFS instances since they start at same time and go outward
        dist = 0
        while q:
            for i in range(len(q)):
                # for each item in the queue 
                r,c = q.popleft()
                # set that room equal to the distance we are at simultaneously
                grid[r][c] = dist

                # add neighbors
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)

            dist +=1





                
                    