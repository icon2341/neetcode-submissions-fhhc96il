from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return true if s2 contains a permulation of s1
        # i.e if any combo of s1 exists as a substring of s2 then return true

        # the easiest way to test this is to use Counter or a freq map once the windows
        # size matches the freq map then we know we are good 2 go

        s1_freq_map = Counter(s1)


        if(len(s2) < len(s1)):
            return False

        l = 0
        r = len(s1)

        while(r <= len(s2)):
            substring = s2[l:r]
            substringFreqMap = Counter(substring)

            print(substringFreqMap,s1_freq_map)
            r+=1
            l+=1
            if(substringFreqMap == s1_freq_map):
                return True
        return False

    
            


        