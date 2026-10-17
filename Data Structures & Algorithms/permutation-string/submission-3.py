class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortedString1 = "".join(sorted(s1))

        l = 0 
        for r in range(len(s1) - 1, len(s2)):
            sortedString2 = "".join(sorted(s2[l:r + 1]))

            if sortedString1 == sortedString2:
                return True 
            l += 1 
        return False 