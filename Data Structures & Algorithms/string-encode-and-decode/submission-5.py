class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in range(len(strs)):
            newString = newString + strs[i] + "~"
        return newString 

    def decode(self, s: str) -> List[str]:
        until = 0 
        arr = []
        for i in range(len(s)):
            if s[i] == "~":
                arr.append(s[until:i])
                until = i + 1
        return arr
