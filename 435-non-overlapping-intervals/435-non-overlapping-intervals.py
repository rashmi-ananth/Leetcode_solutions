class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        print(intervals)
        
#         ----------
#             ----------
            
#         -----
#                 -------
            
            
#         ---------------
#             ------




            
            
        prev = intervals[0]
        counter = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
                
            else:
              #  print(intervals[i], prev)
                if intervals[i][0] >= prev[0] and intervals[i][1] < prev[1]:
                    prev = intervals[i]
                
                counter += 1
                
        return counter       
        
        
#         sorted_intervals = sorted(intervals, key = lambda x:(x[1]))
        
        
#         end = sorted_intervals[0][1]
#         count = 1
#         for i in range(1, len(sorted_intervals)):
#             if sorted_intervals[i][0] >= end:
#                 end = sorted_intervals[i][1]
#                 count += 1
                
#         return len(sorted_intervals) - count
        

        
        
        
        
        
        
        