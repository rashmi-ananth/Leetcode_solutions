from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        counts = defaultdict(int)
        
        for i in range(len(words)):
            counts[words[i]] += 1
              
        
        answer = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        

        return_ans = []
        for i in range(k):
            return_ans.append(answer[i][0])

        return return_ans
            
            
        
        
        
        
        