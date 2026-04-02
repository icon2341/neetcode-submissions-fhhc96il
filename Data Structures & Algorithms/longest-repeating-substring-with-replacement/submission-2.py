class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # you are trying to find the longest string
        # where the counts of each letter type are tabulated
        # and the letters which are not the majority
        # do not exceed k

        substringQuantityMap = {}
        longestSubstring = 0
        startIndex = 0

        for endIndex in range(len(s)):
            currentLetter = s[endIndex]
            # add the new letter to the quantity map
            substringQuantityMap[currentLetter] = substringQuantityMap.get(currentLetter,0)+1

            maxFreq = max(substringQuantityMap.values())
            substringSize = len(s[startIndex:endIndex+1])

            if(substringSize - maxFreq) > k:
                leftChar = s[startIndex]
                substringQuantityMap[leftChar] -=1
                startIndex += 1
            else:
                longestSubstring = max(longestSubstring, substringSize)

        return longestSubstring


