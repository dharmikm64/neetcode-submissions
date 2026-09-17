class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {} 
        arr = []
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in myMap:
                myMap["".join(sorted(strs[i]))].append(strs[i])
            else: 
                myMap["".join(sorted(strs[i]))] = [strs[i]]
        
        for key in myMap: 
            arr.append(myMap[key])
        return arr
        