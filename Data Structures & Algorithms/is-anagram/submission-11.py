class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedValue = sorted(s)
        sortedArr = sorted(t)

        return sortedValue == sortedArr