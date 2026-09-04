class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_amount = 0 
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0 :
                zero_amount += 1
            else: 
                product *= nums[i]
        if zero_amount > 1 :
            return [0] * len(nums)
        
        for i in range(len(nums)):
            if zero_amount != 0: 
                output[i]
                if nums[i] != 0:
                    output[i] = 0
                else:
                    output[i] = product
            else:
                output[i] = product // nums[i] 
        return output


                
                    