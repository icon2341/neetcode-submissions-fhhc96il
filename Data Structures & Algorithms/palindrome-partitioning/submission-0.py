class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Decision, to split or ot to split at each index
        # base case: if we have reached the end of a string means we have made the decision
        # at each index
        # constraint: subsequent string must be a palindrome for us to split first
        

        res = []
        part = []

        def dfs(i):
            # have we made a decision for every index in this string?
            # if so, then append this part to the results
            if i >= len(s):
                res.append(part.copy())
                return
            # loop through each index in tehe substring
            for j in range(i, len(s)):
                # determine if splitting it yields a palindrome
                if self.isPali(s, i, j):
                    # if so then append the split version to the parts
                    part.append(s[i:j+1])
                    # start working on the substring within the partitian
                    dfs(j+1)
                    # back track and remvoe the part as we check wider strings
                    part.pop()

        dfs(0)
        return res

# simple is palindrome algo with 2 pointer approach
    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1, r-1
        return True

