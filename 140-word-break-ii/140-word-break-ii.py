class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        wordSet = set(wordDict)
        
        
        for end in range(1, len(s) + 1):
            sublist = []
            for start in range(0, end):
                
                word = s[start:end]
                if word in wordSet:
                    for i in dp[start]:
                        sublist.append((i + ' ' + word).strip())
            dp[end] = sublist
         
        return dp[len(s)]
                        

