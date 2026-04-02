from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # 1. Count the frequencies of characters we NEED from t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # 2. Setup sliding window variables
        window = {}
        have = 0
        need = len(count_t) # We need this many UNIQUE characters to reach their target frequencies
        
        res = [-1, -1] # [left_index, right_index]
        res_len = float("infinity")
        l = 0

        # 3. Expand the window with the right pointer
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # If we just added a character we need, and its count matches exactly what we need
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # 4. Shrink the window from the left while it remains valid
            while have == need:
                # Update our result if this window is smaller than the current smallest
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop the left character from the window
                left_char = s[l]
                window[left_char] -= 1
                
                # If removing this character breaks our valid window condition
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                l += 1 # Move left pointer forward to shrink

        # 5. Return the substring using the saved pointers
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""

        
        

