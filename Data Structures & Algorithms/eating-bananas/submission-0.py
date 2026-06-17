import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles, h, k):
            hours = 0
            i =0
            #p =(len(piles))
            for i in piles :
                hours += math.ceil(i/k)
            return hours<= h
        
        l, r= 1, max(piles)

        while (l<=r):
            k = (l+r) // 2 
            if canFinish(piles, h, k):
                result = k 
                r = k -1 
            else:
                l = k +1
        
        return result