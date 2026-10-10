class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myMap = defaultdict(list)
        arr = []
        for i in range(len(strs)):
            count = [0] * 26 
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1 
            
            myMap[tuple(count)].append(strs[i])
        
        return list(myMap.values())