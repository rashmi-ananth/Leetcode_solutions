class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        endings = [0] * (len(s) + 1)
        endings[0] = 1
        
        for i in range(len(s)):
            if endings[i] == 1:
                for word in wordDict:
                    if word == s[i:i + len(word)]:
                        endings[i + len(word)] = 1
            
        return endings[-1]
        
        
        




        
        