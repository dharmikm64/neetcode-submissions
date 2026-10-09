class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        arr = [] 
        for i in range(len(strs)):
            sortedString = sorted(strs[i])
            sortedString = " ".join(sortedString)

            if sortedString in myMap: 
                myMap[sortedString].append(strs[i])
            else: 
                myMap[sortedString] = []
                myMap[sortedString].append(strs[i])

        for key in myMap: 
            arr.append(myMap[key])
        return arr