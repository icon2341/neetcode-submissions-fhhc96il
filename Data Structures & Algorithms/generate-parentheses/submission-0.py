class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Decision to open or close a parenthesis
        # constraint we can only open if open < n 
        #  we can only close if close < open
        # base case: we stop when open == close == n

        res = []

        def dfs(index, open_p, close_p, path):
            print(path, open_p, close_p)
            if(open_p == close_p and open_p == n):
                res.append("".join(path[:]))
                return

            # decision to close
            if(close_p < open_p):
                path.append(")")
                dfs(index+1, open_p, close_p+1, path)
                path.pop()
            
            if(open_p < n):
                path.append("(")
                dfs(index+1, open_p+1, close_p, path)
                path.pop()
            

        dfs(0,0,0,[])
        return res
