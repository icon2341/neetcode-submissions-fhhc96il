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
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_end

        return dfs(0, self.root)