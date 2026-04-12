from collections import deque
 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # given grid representing a heights of an island
 
        # island borders pacific from top and left and atlantic fomr bottom and right
 
        # water can flow in four directions up down left right to a cell
        # that is equal or lower
 
        # find all cells where water can flow from both the pacific and atlantic oceans
 
        # intution: We want to find cells that can find any of the cells at 
        # r-1 and c-1
        # AND c = 0 and r = 0
 
        # feels like simultaneous BFS already
        # where we start from the ocean and move backwards into the grid
        # keep two grids called pacificSucc and atlanticSucc
 
        ROWS,COLS = len(heights), len(heights[0])
 
        pq = deque()
        pqV = set()
        pacificSucc = [[False for _ in range(COLS)] for _ in range(ROWS)]
 
 
        def addPQ(old_coord,coord):
            nonlocal pqV
 
            r,c = coord
            r_old, c_old = old_coord
            # check out of bounds
            # check if neighbor is lower
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r_old][c_old] > heights[r][c] or (r,c) in pqV):
                return
 
            pq.append(coord)
            pacificSucc[r][c] = True
 
 
        # loop through and add all pacific Q
        for i in range(len(heights[0])):
            pq.append((0,i))
 
        for i in range(len(heights)):
            pq.append((i,0))
 
        while(pq):
            r,c = pq.popleft()
            pqV.add((r,c))
            pacificSucc[r][c] = True

            addPQ((r,c),(r+1,c))
            addPQ((r,c),(r-1,c))
            addPQ((r,c),(r,c+1))
            addPQ((r,c),(r,c-1))
 
 
        aqV = set()
        aq = deque()
        atlanticSucc = [[False for _ in range(COLS)] for _ in range(ROWS)]
 
        def addAQ(old_coord,coord):
            nonlocal aqV
 
            r,c = coord
            r_old, c_old = old_coord
            # check out of bounds
            # check if neighbor is lower
            print(r,c)
            if(r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r_old][c_old] > heights[r][c] or (r,c) in aqV):
                return
 
            aq.append(coord)
            print(r,c,len(atlanticSucc), len(atlanticSucc[0]), ROWS, COLS)
            atlanticSucc[r][c] = True
 
 
        # loop through and add all pacific Q
        for i in range(len(heights[0])):
            aq.append((ROWS-1,i))
 
        for i in range(len(heights)):
            aq.append((i,COLS-1))
 
        while(aq):
            r,c = aq.popleft()
            aqV.add((r,c))
            atlanticSucc[r][c] = True

            addAQ((r,c),(r+1,c))
            addAQ((r,c),(r-1,c))
            addAQ((r,c),(r,c+1))
            addAQ((r,c),(r,c-1))
 
        print(pacificSucc)
        print(atlanticSucc)
        output = []
 
        for i in range(ROWS):
            for j in range(COLS):
                if(pacificSucc[i][j] and atlanticSucc[i][j]):
                    output.append([i,j])
 
        return output


"Using simultaneous BFS in reverse order was able to do it on my own!"