from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 0:
            return 0
        
        intervals.sort()
        h = [intervals[0][1]]
        counter = 1
        
        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            if new_start >= h[0]:
                heappop(h)
            else:
                counter += 1
            heappush(h, intervals[i][1])
            
            
        return counter
                
            
        
        
        

        
        
        
        
        
        
      
    
    
        
        
        
        
        
        