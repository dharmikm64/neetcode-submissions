class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = [] 
        myMap = {} 


        for i in range(len(numbers)):
            if target - numbers[i] in myMap: 
                arr.append(myMap[target-numbers[i]])
                arr.append(i + 1 )
            else: 
                myMap[numbers[i]] = i + 1
        return arr