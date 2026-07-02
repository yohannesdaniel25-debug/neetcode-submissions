class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #We need to find a minimum that where we can start out window 
        #For the example of 10, 1,5, 7,6,1
        #The window starts at 10 aas our new min
        #We will check if prices[i] < min(Which is 10)
        #New min is now 1(left += 1) that is where out new window will start
        #We will keep checking for min in this window, but we will now start looking for the max_profit
        #window will start as 1, 5 : prices[i] > min
        #Next check if it is the greatest number we have seen in the window
        #if prices[i] > greatest => TRUE= > greatest = 5 =>  Calculate for max profit now
         #now calc for max_profit = 5 -1 = 4 
        #Window will now expand one more, we will check the next number [1, 5, 7]
        #Check if prices[i]< min => FALSE => if prices[i] > greatest = > TRUE
        #Calc for max_profit = 7 - 1 = 6    that is our new max profit 
         #Now out new window is [1, 5 ,7 ,6]
         #Checl for prices[i] < min => FALSE => if prices [i] > greatest => False 
         #Next window is [1, 5, 7,6 ,1] => This will lead us to be finshes and 
         #now we return max_profit which is 6

        l, r, profit, max_profit = 0, 0, 0, 0
        min_price = float('inf')
        for r in range(len(prices)):
            if min_price > prices[r]:
                min_price = prices[r]
                l = r
            profit = prices[r]- min_price
            
            max_profit = max(max_profit, profit)
        return max_profit
            


         
