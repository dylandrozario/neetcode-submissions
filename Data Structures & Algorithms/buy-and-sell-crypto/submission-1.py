class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       #array given is prices per day of a coin
       #must find the case where you return max profit
       #if no profit return 0
       #in my mind I think i will make a lowest counter and highest counter
       #to track the most expensive one and the cheapest one
       #I think I move and if I find something that is on an element to the left greater than
       #we ignore it
       #if left not greater than 
        l = 0
        r = 1
        maximum = 0

        while(r < len(prices)):
            if prices[l] < prices[r]:
                maximum = max(prices[r] - prices[l], maximum)
            else:
                l = r
            r += 1
        
        return maximum
    