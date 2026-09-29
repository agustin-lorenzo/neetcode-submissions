class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))
            if len(w2) < len(w1) and w1[:minLength] == w2[:minLength]:
                return ""

            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = set()
        path = set()
        order = []

        def dfs(c):
            if c in visited:
                return True
            if c in path:
                return False
            
            path.add(c)
            for n in adj[c]:
                if not dfs(n):
                    return False
            path.remove(c)

            visited.add(c)
            order.append(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        order.reverse()
        return "".join(order)