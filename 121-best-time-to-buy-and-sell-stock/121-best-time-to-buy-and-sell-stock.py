class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        difference = 0
        min_val = prices[0]
        
        
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                continue
            difference = max(difference, (prices[i] - min_val))

        return difference
    
    
    
