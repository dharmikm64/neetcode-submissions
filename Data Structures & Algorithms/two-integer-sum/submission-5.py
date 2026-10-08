class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [] 
        myMap = {} 

        for i in range(len(nums)):
                if (target - nums[i]) in myMap:
                    arr.append(myMap[target-nums[i]])
                    arr.append(i)
                else: 
                    myMap[nums[i]] = i 
                   
        
        return arr