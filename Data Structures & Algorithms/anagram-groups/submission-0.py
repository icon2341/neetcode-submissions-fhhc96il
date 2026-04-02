class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordList = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if(sorted_string not in wordList):
                wordList["".join(sorted(string))] = [string]
            else:
                wordList["".join(sorted(string))].append(string)

        output = []
        for group in wordList:
            output.append(wordList[group])

        return output