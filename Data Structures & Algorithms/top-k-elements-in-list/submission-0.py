class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        newArr = []
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1 
            else:
                hashMap[nums[i]] = 1 
        
        if len(hashMap) <= k:
            for key in hashMap: 
                newArr.append(key)
        elif len(hashMap) > k:
            hashMap = dict(sorted(hashMap.items(), key = lambda item : item[1], reverse = True))
            counter = 0 
            for key in hashMap:
                if counter < k:
                    newArr.append(key)
                    counter += 1 
        return newArr

      