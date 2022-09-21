class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        sorted_intervals = sorted(intervals, key = lambda x:(x[1]))
        
        
        end = sorted_intervals[0][1]
        count = 1
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] >= end:
                end = sorted_intervals[i][1]
                count += 1
                
        return len(sorted_intervals) - count
        

        
        
        
        
        
        
        