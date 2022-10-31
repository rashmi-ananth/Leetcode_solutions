class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # Time: O(nlogn)
        # Space: O(N)
        freq = defaultdict(int)
        
        for i in range(len(words)):
            freq[words[i]] += 1
          
        
            
        result = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
        
        return_lst = []
        for i in range(k):
            return_lst.append(result[i][0])
        
        return return_lst
        
        