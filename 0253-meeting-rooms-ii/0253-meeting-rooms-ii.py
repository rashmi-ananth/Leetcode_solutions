from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # time: O(nlogn)
        # Space: O(n)
        
        count = 1
        intervals.sort()
        h = [intervals[0][1]]
        heapify(h)
        
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < h[0]:
                count += 1    
            else:
                heappop(h)
            heappush(h, intervals[i][1])
                
        return count
            
        
        
        
        