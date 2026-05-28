class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                char = word[j]
                if char == '.':
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.endOfWord
        return dfs(0, self.root)

