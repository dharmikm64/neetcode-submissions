class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mySMap = {}
        myTMap = {}

        for i in range(len(s)):
            if s[i] in mySMap: 
                mySMap[s[i]] += 1
            else:
                mySMap[s[i]] = 0 

        for j in range(len(t)):
            if t[j] in myTMap:
                myTMap[t[j]] += 1
            else: 
                myTMap[t[j]] = 0
        
        return myTMap == mySMap