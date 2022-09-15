class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        smallest_buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > smallest_buy:
                max_profit = max(max_profit, prices[i] - smallest_buy)
            else:
                smallest_buy = prices[i]
                
        

                
        return max_profit
    
    
    
    
