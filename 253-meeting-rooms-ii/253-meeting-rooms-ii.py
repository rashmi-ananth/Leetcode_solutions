class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        lst = []
        lst.append(intervals[0][1])
        
        for i in range(1, len(intervals)):

            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            for i in range(len(lst)):
                if curr_start >= lst[i]:
                    lst[i] = curr_end
                    break
            else:
                lst.append(curr_end)
                    

        return len(lst)
                    
            
            