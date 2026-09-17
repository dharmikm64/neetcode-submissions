class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedList = sorted(list(set(nums)))
        max_streak = 1 
        streak = 1 
        if not nums: 
            return 0 
        for i in range(1,len(sortedList)):
            if sortedList[i] == sortedList[i-1] + 1:
                streak += 1
            else: 
                streak = 1 
            max_streak = max(max_streak, streak)
        return max_streak