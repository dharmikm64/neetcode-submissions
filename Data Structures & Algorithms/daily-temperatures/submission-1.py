class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        arr = [] 

        for i in range(len(temperatures)):
            while arr and temperatures[i] > arr[-1][0]:
                item = arr.pop()
                tempStack = item[0]
                indexStack = item[1]
                result[indexStack] = i - indexStack 
            arr.append((temperatures[i], i))
        return result