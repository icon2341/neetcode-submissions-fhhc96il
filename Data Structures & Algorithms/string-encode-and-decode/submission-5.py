class Solution:

    def encode(self, strs: List[str]) -> str:
        outputString = ""

        for string in strs:
            outputString += str(len(string))+'#' + string
        return outputString

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            # SLIDING WINDOW!
            length = int(s[i:j])
            # offset for the string sniping since we do not need the HASHTAG
            i = j+1
            j = i + length 
            res.append(s[i:j]) 
            i = j

        return res
        

                

