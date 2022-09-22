class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        prev = intervals[0]
        counter = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
                
            else:
                if intervals[i][0] > prev[0] and intervals[i][1] < prev[1]:
                    prev = intervals[i]
                
                counter += 1
                
        return counter       
        