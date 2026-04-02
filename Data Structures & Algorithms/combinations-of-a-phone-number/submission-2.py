class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # given digits 2 - 9 string
        # each digit is mapped to set of characters

        # digit hash map

        digit_map = {
            "2": ["A", "B", "C"],
            "3": ["D", "E", "F"],
            "4": ["G", "H", "I"],
            "5": ["J", "K", "L"],
            "6": ["M", "N", "O"],
            "7": ["P", "Q", "R", "S"],
            "8": ["T", "U", "V"],
            "9": ["W", "X", "Y", "Z"],
        }

        # decision: Which letter to choose at each index
        # base case, we have made a decision for all indexes

        res = []

        if not len(digits):
            return []

        def dfs(i, path):
            if(i >= len(digits)):
                res.append(("".join(path[:])).lower())
                return

            choices = digit_map[digits[i]]

            for choice in choices:
                path.append(choice)
                dfs(i+1, path)
                path.pop()

        dfs(0,[])
        return res


