class TrieNode:
    def __init__(self):
        # OPTIMIZATION: You can do ord(a) - ord(letter)
        # to store everything in a 25 char array for quick lookups instead of a dict
        self.children = {}
        self.is_end = False
        self.visit_count = 0

    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # MASS -> ASS -> SS -> S
    def add_word_prefix(self,word):
        # simple just traverse root again for each prefix of the word
        for i in range(len(word)):
            cur = self.root
            subWord = word[i:]
            for letter in subWord:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
                cur.visit_count += 1

            cur.is_end = True

    # traverse the trie using the word, if the node that is at the 
    # last letter of the word's Tries count is greater than 1 then return True
    def search_for_word(self, word):
        cursor = self.root
        for letter in word:
            if(letter not in cursor.children):
                return False
            else:
                cursor = cursor.children[letter]
        if(cursor.visit_count > 1):
            return True
        else:
            return False

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # The brute force solution 
        # is to take a word i
        # then look through every other word j, and do a 2 pointer approach idx and jdx
        # where you advance both pointers if they are equal
        # but we reset the idx pointer every time they aren't
        # if we completely get through word I for any of the words then we know its a 
        # subset and we can add it to our output array.
        # this is O(n^2) though

        # using a Trie we can solve this problem
        # we insert words into the trie
        # each node tracks how many times its been visited
        # if the final node in any word has bee nvisted more than once
        # the word is a substring in another word
        # essentially for Neetcode
        # and code
        # for a suffix tree, instead of containing one word such as MASS
        # you would store 
        # MASS, ASS, SS,S
        # Then finally, you traverse it with your eval word such as "as"
        # as will end up on S in ASS, you will then see that the S has a visited of 2
        # 1 for mass and 1 for as when we inserted it
        # this means that "as" must be a substring of "mass"
        # this is because when we build the prefix trie, we dont build redundant branches
        # as doesnt have its own branch and would be put inside MASS -> ASS

        trie = Trie()
        res = []
        for word in words:
            trie.add_word_prefix(word)
        
        for word in words:
            result = trie.search_for_word(word)
            print(result)
            if(result):
                res.append(word)

        return res



