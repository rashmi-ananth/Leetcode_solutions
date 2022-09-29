class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        arr = [None] * (len(s) + 1)
        arr[0] = [""]
        
        
        for i in range(len(s)):
            if arr[i] != None:
                for word in wordDict:
                    if word == s[i:i+len(word)]:
                        if arr[i+len(word)] == None:
                            arr[i+len(word)] = []
                        
                        for sub in arr[i]:
                            arr[i+len(word)].append((sub + " " + word).strip())
        
        return arr[-1]
        
        
        
         
        
        
        
        
        