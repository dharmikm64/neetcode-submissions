class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {"}" : "{", "]" : "[", ")" : "("}

        arr = []

        for i in range(len(s)):
            if s[i] in myMap:
                if arr and arr[-1] == myMap[s[i]]:
                    arr.pop()
                else: 
                    return False

            else: 
                arr.append(s[i])
        if not arr: 
            return True
        else: 
            return False