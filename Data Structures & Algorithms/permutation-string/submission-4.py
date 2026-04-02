class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return true of s2 contains a permutation of s1
        # meaning, determine if any the combinations of s1 are in s2
        # we need to take "slices" of s2 and see if any of the len(s1) letter slices
        # contain ALL the letters of s1.
        # The best way to do this is to convert each slice to a set, and see if it 
        # equals the set that is s1

        s1FrequencyMap = {}

        for letter in s1:
            s1FrequencyMap[letter] = s1FrequencyMap.get(letter,0) + 1

        if(len(s2) < len(s1)):
            return False
        startIndex = 0
        print(len(s2)-len(s1))

        while(startIndex < len(s2)):


            substringS2 = s2[startIndex:startIndex+len(s1)]
            substringS2Freq = {}
            for letter in substringS2:
                substringS2Freq[letter] = substringS2Freq.get(letter, 0) +1
            # set does not work because we are forgetting when multiple letters are in teh same substring

            print(s1,substringS2,startIndex,startIndex+len(s1))

            if(substringS2Freq == s1FrequencyMap):
                return True
            startIndex += 1

        return False
            


        