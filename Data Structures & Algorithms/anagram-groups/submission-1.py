class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        removed = []
        for i in range(len(strs)):
            if i in removed:
                continue
            iAnagramList = [strs[i]]
            for j in range(i+1, len(strs)):
                if len(strs[i]) != len(strs[j]):
                    pass                    
                else:
                    iMap, jMap = {}, {}
                    for k in range(len(strs[i])):
                        iMap[strs[i][k]] = 1+ iMap.get(strs[i][k], 0)
                        jMap[strs[j][k]] = 1+ jMap.get(strs[j][k], 0)
                    if iMap == jMap:
                        iAnagramList.append(strs[j])
                        removed.append(j)
            result.append(iAnagramList)
        return result

