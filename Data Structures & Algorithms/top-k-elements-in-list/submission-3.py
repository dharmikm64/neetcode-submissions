class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myMap = {} 
        for i in range(len(nums)):
            if nums[i] in myMap:
                myMap[nums[i]] += 1 
            else: 
                myMap[nums[i]] = 1 
        
        counter = 0 
        myMax = 0 
        arr = []
        while counter < k:
            myMax = max(myMap.values())
            for key in myMap:
                if myMax == myMap[key]:
                    arr.append(key)
                    myMap.pop(key)
                    break
            counter += 1 
            
        return arr 