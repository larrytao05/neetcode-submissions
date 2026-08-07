class TrieNode:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            if i == len(word)-1:
                cur.isWord = True
        
    
    def prefix(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return False
            cur = cur.children[c]
    
    def contains_word(self, word):
        cur = self.root
        for i,c in enumerate(word):
            if c not in cur.children:
                return False
            if i == len(word)-1 and not cur.isWord:
                return False
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        res = set()
        visit = set()
        m = len(board)
        n = len(board[0])
        def dfs(i,j,acc, node):
            if not (0 <= i < m) or not (0 <= j < n) or (i,j) in visit or board[i][j] not in node.children:
                return
            acc+= board[i][j]
            visit.add((i,j))
            node = node.children[board[i][j]]
            if node.isWord:
                res.add(acc)
            for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                nr,nc = i + dr, j + dc
                dfs(nr,nc,acc,node)
            visit.remove((i,j))

        for i in range(m):
            for j in range(n):
                dfs(i,j,"",trie.root)
        return list(res)
            

        