class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""

        for i in range(len(strs[0])):
            curr = strs[0][i]

            for j in range(len(strs)):
                if i > len(strs[j]) - 1:
                    return answer

                if strs[j][i] != curr:
                    return answer
                
            answer += curr
        
        return answer