class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1
        max = 0

        while l < r:
            #Find the area of the curr positions
            curr = (r- l) * min(heights[l], heights[r])
            #Check if the current area is greater than the prev max
            if curr > max:
                max = curr
            

            #either increment or decrement the smaller heights of the left and right respectivley 
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return max
            

            
            