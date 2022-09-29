class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # ---------------4
#             --------------------
            
#         ------ ---------4
        
#         ------------------
#             -------4
            
            
        intervals.sort()
        prev = intervals[0]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
                continue
            elif prev[1] > intervals[i][1]:
                prev = intervals[i]
            count += 1
            
        return count
                
            
                
                
            
            
            
            
            
            
            
            
            
            
        