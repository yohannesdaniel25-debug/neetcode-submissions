class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute force
        i=0
        min = nums[i]
        c= len(nums)
        for i in range (len(nums)):
            if nums[i] <= min:
                min = nums[i]
            else:
                continue       
        return min
