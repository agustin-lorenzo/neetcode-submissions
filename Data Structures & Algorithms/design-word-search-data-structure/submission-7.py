class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i >= len(word):
                return node.end
            
            c = word[i]
            if c == '.':
                for n in node.child.values():
                    if dfs(n, i + 1):
                        return True
                return False
            
            if c in node.child:
                return dfs(node.child[c], i + 1)
            return False
        
        return dfs(self.root, 0)
