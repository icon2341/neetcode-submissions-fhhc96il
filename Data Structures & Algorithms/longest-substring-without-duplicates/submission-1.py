class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longestSubstring = 0
        startIndex = 0
        
        # We iterate with endIndex as the leading edge
        for endIndex in range(len(s)):
            # If the character is already in our window, 
            # shrink the window from the left
            while s[endIndex] in s[startIndex:endIndex]:
                startIndex += 1
            
            # Calculate the current window length: (endIndex - startIndex + 1)
            current_len = endIndex - startIndex + 1
            if current_len > longestSubstring:
                longestSubstring = current_len

        return longestSubstring