class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = []
        
        for i in range(len(timePoints)):
            hours, mins = timePoints[i].split(':')
            times.append((int(hours) * 60) + int(mins))
            
        times.sort()
        
        min_time = 60 * 24
        for i in range(len(times) - 1):
            curr_min = times[i+1] - times[i]
            min_time = min(min_time, curr_min)
            
        
            
        min_time = min(min_time, (60*24 - times[-1]) + times[0])
        return min_time
            
            
            