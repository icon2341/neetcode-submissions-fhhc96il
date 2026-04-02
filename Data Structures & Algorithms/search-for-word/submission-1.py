class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Decision up down left right
        # Constraint within board dimensions, may not use same cell twice in word
        # base case length of path is larger than len(word) False
        # base case word == path True


        # tricks:
        # we use a visited array to track where we have been


        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,i):
            # given that we only pick valid choices, if we somehow 
            # get to the length of the word. That means that our path is valid
            # therefore we have found the word
            if(i == len(word)):
                return True
            """
            If we are out of bounds, or if the letter we are looking at does not match the coresp. letter of the word (since we track index)
            or if this node has already been visited in a previous path since it would already be marked True in the visited array
            then we know this is an invalid base case
            """
            if(r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[i] != board[r][c] or visited[r][c]):
                return False

            # otherwise continue and set this to true
            visited[r][c] = True
            # do a branch at each neighbor, we dont care which one is true we are happy with either.
            res = dfs(r+1,c, i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            # backtrack setting this to false so it can be used down the road.
            visited[r][c] = False
            return res

        # we need to run this for each item on the board to pick a new starting config
        # each time.
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        # if none of the start configs returned true then we know our answer is false.
        return False
         