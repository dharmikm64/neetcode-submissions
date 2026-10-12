class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mySet = set()
        length = 0 
        myMax = 0 
        l = 0 
        for r in range(len(s)):

            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1 
            mySet.add(s[r])
            myMax = max(myMax, len(mySet))

        return myMax