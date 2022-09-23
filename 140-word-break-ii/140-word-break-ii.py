class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        arr = [None] * (len(s) + 1)
        arr[0] = [[]]
        wordSet = set(wordDict)
        # print(len(arr[0]), len(arr[1]))
        
      #  [[cats, and], [cat, sand]], 
        
        
        print(arr)
        
        for i in range(len(s) + 1):
            for word in wordSet:
               # print(s[i], word, s[i: i + len(word)], word == s[i: i + len(word)])
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    # print(word)
                    
                    if arr[i] == None:
                        continue
                    for k in arr[i]:
                        if arr[i+len(word)] == None:
                            arr[i+len(word)] = []
                        arr[i+len(word)].append(k + [word])
        
        if arr[-1] == None:
            return []
        return_arr = []
        print(arr)
        for i in arr[-1]:
            return_arr.append(' '.join(i))
        
        return  return_arr
        
        
        
        
        
        
        