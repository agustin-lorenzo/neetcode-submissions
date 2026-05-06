class TrieNode():

    def __init__(self):
        self.child = {}
        self.end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        root = TrieNode()
        result = set()

        # add all words to a prefix tree
        for word in words:
            curr = root
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
            curr.end = True
            curr.word = word
        
        # dfs for checking a given character at every cell
        visited = set()
        def dfs(r, c, node):
            if node.end:
                result.add(node.word)

            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                board[r][c] not in node.child):
                return
            
            nxt = node.child[board[r][c]]
            visited.add((r, c)) # use backtracking with visited to avoid using same cell twice in current path
            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)
            visited.remove((r, c))
            return
        
        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return list(result)
