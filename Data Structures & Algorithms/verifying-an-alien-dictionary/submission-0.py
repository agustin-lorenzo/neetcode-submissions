class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1), len(w2))

            if len(w2) < len(w1) and w1[:minLength] == w2[:minLength]:
                return False
            
            for j in range(minLength):
                if w1[j] != w2[j]:
                    if rank[w2[j]] > rank[w1[j]]:
                        break
                    else:
                        return False
        
        return True
