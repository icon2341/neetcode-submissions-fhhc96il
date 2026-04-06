class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")

        lastWord = ""
        for word in words:
            if(word != " " and word != ""):
                lastWord = word

        return len(lastWord)