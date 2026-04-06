class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cursor = self.root
        for letter in word:
            if(letter in cursor.children):
                cursor = cursor.children[letter]
            else:
                cursor.children[letter] = TrieNode()
                cursor = cursor.children[letter]
        cursor.is_end = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # build a trie of each one
        trie = Trie()

        for word in strs:
            trie.addWord(word)
        
        # loop through trie until you recieve a multi child option then return
        prefix = ""

        trieCursor = trie.root
        while(len(trieCursor.children.keys()) == 1 and trieCursor.is_end == False):
            value = list(trieCursor.children.keys())[0]
            print(list(trieCursor.children.keys()))
            trieCursor = trieCursor.children[value]
            prefix += value

        return prefix
