from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # intuition,
        # find an island by finding an O
        # traverse it with a visited set and check to see 
        # if at any point the o is on a border
        # if it is, then we know that island is dead not surrounded

        # alternatively, we want to find all border O since we know those are not surrounded
        # traverse all Os that touch them
        # mark all of those Os as B
        # then go through the board n^2 and find all remaining
        # os turn them into X
        # and then find all remaining B, turn them into O

        q = deque()

        ROWS = len(board)
        COLS = len(board[0])

        # loop through and add all Os on edges to board
        
        # top and bottom
        for col in range(COLS):
            if(board[0][col] == "O"):
                q.append((0,col))
            if(board[ROWS-1][col] == "O"):
                q.append((ROWS-1, col))

        # left and right
        for row in range(ROWS):
            if(board[row][0] == "O"):
                q.append((row,0))
            if(board[row][COLS-1] == "O"):
                q.append((row,COLS-1))

        def addPoint(coord):
            r,c = coord

            # check if out of bounds or marked B or marked X
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "B" or board[r][c] == "X"):
                return
            board[r][c] = "B"
            q.append((r,c))

        
        # simultaneous BFS on each border O, mark B as we go
        while(q):
            r,c = q.popleft()

            board[r][c] = "B"

            addPoint((r+1,c))
            addPoint((r-1,c))
            addPoint((r,c+1))
            addPoint((r,c-1))

        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] == "B"):
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
            



        