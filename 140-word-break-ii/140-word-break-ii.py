class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        
     # [""] [] [] ["cat"] [ "cats"] [] [] ["cat sand", "cats and"] [] [] ["cat sand dog", "cats and dog"] []
        
        dp = [[]] * (len(s) + 1)
        dp[0] = [""]
        wordSet = set(wordDict)
        for end in range(1, len(s) + 1):
            sublist = []
            for start in range(0, end):
                word = s[start:end]
                if word in wordSet:
                    for j in dp[start]:
                        sublist.append((j + ' ' + word).strip())
            dp[end] = sublist
            
        print(dp)    
        return dp[len(s)]
                        
                    