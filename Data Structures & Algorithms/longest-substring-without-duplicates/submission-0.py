class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myMap = {} 
        l = 0
        maximum = 0
        for i in range(len(s)):
            if s[i] in myMap and myMap[s[i]] >= l:
                l = myMap[s[i]] + 1

            myMap[s[i]] = i
            maximum = max(maximum, i - l + 1) 
        return maximum