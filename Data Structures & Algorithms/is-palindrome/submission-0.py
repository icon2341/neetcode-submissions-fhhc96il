class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverseString = ""

        for letter in s:
            if letter.isalnum():
                reverseString += letter

        cleanedString = ""

        for letter in s[::-1]:
            if letter.isalnum():
                cleanedString += letter

        print(reverseString, '\n', cleanedString)
        return reverseString.lower() == cleanedString.lower()