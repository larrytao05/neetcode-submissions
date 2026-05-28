class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        def createTrie():
            trie = Trie()
            for word in words:
                trie.insert(word)
            return trie
        trie = createTrie()
        def dfs(x,y, root):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return
            curr = root
            char = board[x][y]
            if char == '#' or char not in curr.children:
                return
            curr = curr.children[char]
            if curr.is_end_of_word:
                res.append(curr.word)
                curr.is_end_of_word = False
            temp = char
            board[x][y] = '#'
            dfs(x+1,y,curr)
            dfs(x-1,y,curr)
            dfs(x,y+1,curr)
            dfs(x,y-1,curr)
            board[x][y] = temp
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,trie.root)
        return res