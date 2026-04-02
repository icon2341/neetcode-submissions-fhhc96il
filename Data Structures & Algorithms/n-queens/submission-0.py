class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        We can simplify this problem:

        We know that each Q must be on a different row, meaning the thing we advance in our "path" 
        is the row

        This means our base case is when our path length (row) == n meaning we have traversed the board
        and we are now out of bounds

        This means the Decision is to place a queen on one of the n cols in the row i.e our choices 
        are each n column

        the constraint is that, we can only place the queen in a column if the position is VALID
        We can determine if a position is valid by keeping track of consumed columns, track of consumed diagonals

        We do that using a clever trick using r-c or r+c which is a unique property of the diags that 
        allows us to assign each diagonal an ID.

        
        """


        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        col = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):

            # are we out of bounds, if so copy it over in the format they want 
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # if the c is taken, or the pos id or neg id for diags is taken then skip this col
                if(c in col) or (r+c  in posDiag ) or ((r-c) in negDiag):
                    continue

                # add the cols and set board
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                # back track
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "." 
        backtrack(0)
        return res