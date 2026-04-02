class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark end of word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # loop through tree hashes until you find that a letter is not 
        #  in childeren

        node = self.root

        for letter in word:
            if(letter not in node.children):
                node.children[letter] = TrieNode()
            
            node = node.children[letter]
        
        node.is_end_of_word = True
                


    def search(self, word: str) -> bool:
        node = self.root

        for letter in word:
            if(letter not in node.children):
                return False
            node = node.children[letter]
            
        if(not node.is_end_of_word):
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for letter in prefix:
            if(letter not in node.children):
                return False
            node = node.children[letter]

        return True

# trie is just a tree
# but instead of using left right etc
# it contains hash map to each letter
# who has a hashmap of its own

