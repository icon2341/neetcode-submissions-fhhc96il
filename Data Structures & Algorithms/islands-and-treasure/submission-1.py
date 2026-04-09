class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])



        # traversal that will find nearest treasure
        # doesnt need to be recursvie
        def findTresure(coord):
            queue =[(coord[0],coord[1],0)]
            visited = set()

            while(queue):
                row,col,distance = queue.pop(0)

                # check if out of bounds or visited or water
                if(row < 0 or row == ROWS or col < 0 or col == COLS or (row,col) in visited or grid[row][col] == -1):
                    continue
                else:
                    visited.add((row,col))
                
                if(grid[row][col] == 0):
                    return distance

                queue.append((row+1,col,distance+1))
                queue.append((row-1,col,distance+1))
                queue.append((row,col+1,distance+1))
                queue.append((row,col-1,distance+1))

            return 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==-1 or grid[i][j] == 0):
                    continue
                grid[i][j] = findTresure((i,j))


                
                    