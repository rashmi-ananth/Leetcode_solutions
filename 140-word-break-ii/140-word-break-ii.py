class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        arr = [None] * (len(s) + 1)
        arr[0] = [[]]
        
        for i in range(len(s) + 1):
            if arr[i] != None:
                for word in wordDict:
                    if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                        for k in arr[i]:
                            if arr[i+len(word)] == None:
                                arr[i+len(word)] = []
                            arr[i+len(word)].append(k + [word])
        
        if arr[-1] == None:
            return []
        return_arr = []
        for i in arr[-1]:
            return_arr.append(' '.join(i))
        
        return  return_arr
        
        
        
        
        
        
        