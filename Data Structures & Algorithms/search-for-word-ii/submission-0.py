class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

    def addWord(self, word):
        cur = self
        for letter in word:
            if(letter in cur.children):
                cur = cur.children[letter]
            else:
                cur.children[letter] = TrieNode()
                cur = cur.children[letter]
        cur.is_end = True
                


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a Trie of the word list
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # we want to do dfs w/ backtracking on each node
        # the dfs adds all neighbors
        # however it will return base case if the node 
        # being evaluated is not in the childeren of the trie
        # i.e traverse trie simultaneously as we traverse each path in BFS

        ROWS, COLS = len(board), len(board[0])
        res,visit = set(), set()

        # each dfs node knows where we are, the Trie node, and the word built upto that point
        def dfs(r,c, node, word):
            # base case if out of bounds, visited, or it is not in the trie when we expect.
            # node in this case is technically parent of the level which we are evaluating in the Trie.
            # so we expect to see this value in the children of that node.
            if(r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children):
                return

            # add this node to visited
            visit.add((r,c))
            # move to the next node to test and add this letter to the word
            node = node.children[board[r][c]]
            word += board[r][c]

            # KEY: if this node is the end, then we know that 
            # we have created a word, we would not be able to get here
            # if the base case (is in trie) let us
            if(node.is_end):
                res.add(word)

            # add neighbors to stack
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)
