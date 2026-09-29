class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adj = defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                adj[pattern].append(w)
        
        q = deque([beginWord])        
        visited = set([beginWord])
        length = 0
        while q:
            length += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return length

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neigh in adj[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
        
        return 0