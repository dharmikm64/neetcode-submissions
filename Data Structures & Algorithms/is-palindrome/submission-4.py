class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedString = ""

        for i in range(len(s)):
            if s[i].isalnum():
                reversedString += s[i]
        

        reversedStringg = reversedString[::-1]
        print(reversedStringg)
        
        return reversedStringg.lower() == reversedString.lower()   