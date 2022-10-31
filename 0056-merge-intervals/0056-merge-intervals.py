class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        return_lst = []
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                return_lst.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        
        return_lst.append([start, end])
        return return_lst
                
        
        
        
# start = 8
# end = 10
# return_lst = [[1,6],[8,10]]
        
#         ____ 
#               ______
            
        
#         _____
#             _____
            
        
#         _____________
#             ______
        