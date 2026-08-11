class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in hashMap and i != hashMap[y]:
                return [i, hashMap[y]]
        
 
        