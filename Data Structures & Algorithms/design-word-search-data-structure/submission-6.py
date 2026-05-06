class TrieNode():
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
            
            if word[i] == '.':
                for c in node.child:
                    if dfs(node.child[c], i + 1):
                        return True
                return False
            
            if word[i] in node.child:
                return dfs(node.child[word[i]], i + 1)
            
            return False
        
        return dfs(self.root, 0)