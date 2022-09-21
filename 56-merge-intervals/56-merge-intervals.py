class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        return_lst = [intervals[0]]
        
        
        
        for i in range(1, len(intervals)):
            if return_lst[-1][1] >= intervals[i][0]:
                return_lst[-1][1] = max(return_lst[-1][1], intervals[i][1])
            else:
                return_lst.append(intervals[i])
                
                
        return return_lst
                
            
        