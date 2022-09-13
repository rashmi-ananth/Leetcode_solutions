class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        
        slots1.sort()
        slots2.sort()
        
        ptr1 = 0
        ptr2 = 0
        
# [[10,50],[60,120],[140,210]]
# [[0,15],[60,70]]
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            start = max(slots1[ptr1][0], slots2[ptr2][0])
            end = min(slots1[ptr1][1], slots2[ptr2][1])
            
            if end - start >= duration:
                return [start,start + duration]
            


            if slots1[ptr1][1] < slots2[ptr2][1]:
                ptr1 += 1

            else:
                ptr2 += 1  
                
        return []
                
                        
                        
                        
                        
            
        