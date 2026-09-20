class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        index = -1
        myMap = {}
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0 :
                product *= nums[i]
            elif nums[i] == 0 :
                myMap[i] = 1
        for i in range(len(output)):
            if len(myMap) > 1 :
                output[i] = 0
            elif len(myMap) == 1 : 
                if i in myMap: 
                    output[i] = product
                else: 
                    output[i] = 0
            else: 
                output[i] = product//nums[i]

        return output 