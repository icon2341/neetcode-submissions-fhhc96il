class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0


        for row in range(ROWS):
            for col in range(COLS):
                # if this isnt a 1, dont start here
                # if its been visited, dont start here
                if(grid[row][col] != 1 or (row,col) in visited):
                    print("SKIPPING", grid[row][col], row, col, (row,col) in visited)
                    continue

                islands +=1
                sizeOfIsland = 0

                stack = [(row,col)]

                print("NEW START")

                while(stack):
                    r,c = stack.pop()
                    # if we are out of bounds or if this node has been visited
                    # exit out of this while loop
                    if(r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in visited or grid[r][c] != 1):
                        print("INVALID: ", r,c)
                        continue
                    else:
                        visited.add((r,c))
                        print("VALID: ", (r,c),grid[r][c] )
                        sizeOfIsland +=1

                        stack.append((r+1,c))
                        stack.append((r-1,c))
                        stack.append((r,c+1))
                        stack.append((r,c-1))

                print("SIZE: ", sizeOfIsland)

                if(sizeOfIsland > res):
                    res = sizeOfIsland 

                


        return res
