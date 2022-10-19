class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        minutes = []
        
        for i in timePoints:
            hour, mins = i.split(':')
            total_mins = int(mins) + (60 * int(hour))
            minutes.append(total_mins)
            
        minutes.sort()
        min_diff = 60 * 24
        
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)
        
        last_diff = ((60 * 24) - minutes[-1]) + minutes[0]
        min_diff = min(min_diff, last_diff)
        
        return min_diff
        
        