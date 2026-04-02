class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        if(len(s) != len(t)):
            return False

        for letter in s:
            if letter not in s_map.keys():
                s_map[letter] = 1
            else:
                s_map[letter] += 1
        
        for letter in t:
            if letter not in s_map.keys():
                return False
            else:
                if letter not in t_map.keys():
                    t_map[letter] = 1
                else:
                    t_map[letter] += 1
                if t_map[letter] > s_map[letter]:
                    return False
        
        return True
        