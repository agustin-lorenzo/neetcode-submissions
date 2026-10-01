class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(set)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                adj[pattern].add(w)
        
        q = deque([beginWord])
        visited = set([beginWord])

        result = 0
        while q:
            result += 1

            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return result

                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for neighbor in adj[pattern]:
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
        
        return 0
