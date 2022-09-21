class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        
        
        
        slots1.sort()
        slots2.sort()
        
        ptr1, ptr2 = 0, 0
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            
            if min(slots1[ptr1][1], slots2[ptr2][1]) - max(slots1[ptr1][0], slots2[ptr2][0]) >= duration:
                return [max(slots1[ptr1][0], slots2[ptr2][0]), max(slots1[ptr1][0], slots2[ptr2][0]) + duration]
            
            elif slots1[ptr1][1] > slots2[ptr2][1]:
                    ptr2 += 1
                    
            else:
                ptr1 += 1
                
        
        return []
            
            
        
        
#         [10,50],[60,120],[140,210]
#         [0,15],[60,70] 
        
        
#         min(end) - max(start) >= duration
        