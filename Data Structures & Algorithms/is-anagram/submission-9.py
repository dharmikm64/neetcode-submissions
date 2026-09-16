class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        name1 = sorted(s)
        name2 = sorted(t)

        return name1 == name2