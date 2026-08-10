class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        return self.search_helper(cur, word, 0)
    
    def search_helper(self, cur, word, idx):
        if not word:
            return cur.isEnd
        for i in range(idx, len(word)):
            c = word[i]
            if c == '.':
                for c in cur.children:
                    if self.search_helper(cur.children[c], word, i+1):
                        return True
                return False
            elif c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
