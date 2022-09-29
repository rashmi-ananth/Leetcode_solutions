class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        
        # sort both slots based on first id
        # compare max(start) min(end) > dur
        # return
        # else update ptr to one that ends earlier
        
        slots1.sort()
        slots2.sort()
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            start = max(slots1[ptr1][0], slots2[ptr2][0])
            end = min(slots1[ptr1][1], slots2[ptr2][1])
            if end - start >= duration:
                return [start, start + duration]
            
            else:
                if slots2[ptr2][1] < slots1[ptr1][1]:
                    ptr2 += 1
                else:
                    ptr1 += 1
             
        return []
        
        