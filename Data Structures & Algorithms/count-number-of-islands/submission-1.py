class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we keep track of places we have been
        # and we traverse from every node that is a 1
        # if we ever come into contact with a place that we have been before
        # Then we know we are part of that island and we can stop.
        # if we find a place we have not been before, We atart that as a new island
        # increase the counter and traverse as normal.
        # we do this for all 1s and return the value

        # traversal logic:
        # traverse all neighbors up down left right
        # if a neigbor has been visited stop traversing


        visited = set()
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])


        for row in range(ROWS):
            for col in range(COLS):
                # if this isnt a 1, dont start here
                # if its been visited, dont start here
                if(grid[row][col] != "1" or (row,col) in visited):
                    print("SKIPPING", grid[row][col], row, col, (row,col) in visited)
                    continue

                islands +=1

                stack = [(row,col)]

                print("NEW START")

                while(stack):
                    r,c = stack.pop()
                    # if we are out of bounds or if this node has been visited
                    # exit out of this while loop
                    if(r >= ROWS or r < 0 or c >= COLS or c < 0 or (r,c) in visited or grid[r][c] != "1"):
                        print("INVALID: ", r,c)
                        continue
                    else:
                        visited.add((r,c))
                        print("VALID: ", (r,c),grid[r][c] )

                        stack.append((r+1,c))
                        stack.append((r-1,c))
                        stack.append((r,c+1))
                        stack.append((r,c-1))


        return islands

                    

                    
            

            
