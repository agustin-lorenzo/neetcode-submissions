from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                adj[pattern].append(w)
        
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        result = 0
        while q:
            result += 1
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return result

                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for n in adj[pattern]:
                        if n in visited:
                            continue
                        q.append(n)
                        visited.add(n)
        return 0
