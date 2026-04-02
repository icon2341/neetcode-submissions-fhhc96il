class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # you are trying to find the longest string
        # where the counts of each letter type are tabulated
        # and the letters which are not the majority
        # do not exceed k

        subStringQuantityMap= {}
        longestSubstring = 0
        startPoint = 0

        for endPoint in range(len(s)):

            # add this to our quantity map
            currentChar = s[endPoint]
            subStringQuantityMap[currentChar] = subStringQuantityMap.get(currentChar, 0) + 1

            # get the most occuring letter
            maxFreq = max(subStringQuantityMap.values())
            currentWindowLength = endPoint - startPoint + 1

            # check if the remaining letters that arent most freq can be subbed
            if(currentWindowLength - maxFreq > k):
                # if not
                leftChar = s[startPoint]
                subStringQuantityMap[leftChar] -=1
                startPoint += 1

            else:
                longestSubstring = max(longestSubstring, currentWindowLength)
        return longestSubstring


