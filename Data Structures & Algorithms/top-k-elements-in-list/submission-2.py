class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myMap = {} 
        arr = []
        for i in range(len(nums)):
            if nums[i] in myMap:
               myMap[nums[i]] += 1  
            else:
                myMap[nums[i]] = 1
        counter = 0 

        while counter < k: 
            maximum = 0
            theKey = 0
            maximum = max(myMap.values())
            for key in myMap:
                if myMap[key] == maximum:
                    theKey = key 
            arr.append(theKey)
            myMap.pop(theKey)
            counter += 1 
        return arr
