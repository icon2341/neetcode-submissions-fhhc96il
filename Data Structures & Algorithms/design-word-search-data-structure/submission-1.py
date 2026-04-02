class TrieNode:

    def __init__(self, val=None, is_end=False):
        self.value = val
        self.is_end = is_end
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cursor = self.root
        for letter in word:
            if letter in cursor.children:
                cursor = cursor.children[letter]
            else:
                cursor.children[letter] = TrieNode(letter, False)
                cursor = cursor.children[letter]
        cursor.is_end = True

    def search(self, word: str) -> bool:
        def dfs(remaining_word, root):
            if(not remaining_word):
                return root.is_end

            char = remaining_word[0]
            suffix = remaining_word[1:]

            if(char == "."):
                for child in root.children.values():
                    # if any of these are true then pass it down
                    if dfs(suffix, child):
                        return True
                # if we dound nothing then return false
                return False
            else:
                # Direct match: Move to the specific child if it exists
                if char in root.children:
                    return dfs(suffix, root.children[char])
                return False
            

        return dfs(word, self.root)