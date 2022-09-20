class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
  
        dp = [0] * (len(s) + 1)
        wordSet = set(wordDict)
        dp[0] = True

        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
                    
        return dp[len(s)]
            
    
    
        #   1   0   1   0   0   0   0   0   0   0
            
            
            
            