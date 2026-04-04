class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # we are given 2 strings s and t lowercase english
        # return the minimum number of chars that need to be appended to the end of 
        # s so t is a subsequence of s

        # subsequence is a string that can be derrived fom another string
        # by deleting some or no chars but not changing the order

        # coaching
        # coding

        sP = 0
        tP = 0

        while(sP < len(s) and tP < len(t)):
            if(s[sP] == t[tP]):
                tP+=1
            sP +=1

        return len(t[tP:])