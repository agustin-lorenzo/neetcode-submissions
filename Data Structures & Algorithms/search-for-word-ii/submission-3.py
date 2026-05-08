class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
            curr.end = True
            curr.word = word
        
        R, C = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node):
            if node.end:
                result.add(node.word)
            
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                board[r][c] not in node.child):
                return
            
            visited.add((r, c))
            char = board[r][c]
            dfs(r + 1, c, node.child[char])
            dfs(r - 1, c, node.child[char])
            dfs(r, c + 1, node.child[char])
            dfs(r, c - 1, node.child[char])
            visited.remove((r, c))
        
        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return list(result)