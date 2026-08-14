class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        num_length = len(nums)
        output = []
        
        #iterating over the given array nums
        for i in range(num_length):
            #since it is SORTED if the first number is positive, there is no answer
            if nums[i] > 0:
                break
            #if i has moved onto the next element, but it is same as previous move i
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            #setting low to 1 more than i
            low = i + 1
            #setting high to the last value in the array
            high = num_length - 1

            # using two pointer if low is less than high
            while low < high:
                #summing up number at i, low, and high to check if it equals 0
                sum = nums[i] + nums[low] + nums[high]
                ## if its zero then we append it to the main list and increment 
                if sum == 0:
                    output.append([nums[i], nums[low], nums[high]])
                    #incrementing low by 1 and high by -1 so they squeeze to middle
                    low += 1
                    high -= 1
                    #if the number at low is equal to low -1 then move up low by one
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    #if the number at high is equal to high +1 move down high by one
                    while low < high and nums[high] == nums [high +1]:
                        high -= 1
                #if sum is less than zero then move up to find a higher number
                elif sum < 0:
                    low  += 1
                #if sum is higher than zero, move the high pointer down to find low #
                elif sum > 0:
                    high -= 1
        #return the final list.
        return output
 
