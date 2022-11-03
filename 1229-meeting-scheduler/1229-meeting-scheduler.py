class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        ptr1, ptr2 = 0, 0
        slots1.sort()
        slots2.sort()
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            max_start = max(slots1[ptr1][0], slots2[ptr2][0])
            min_end = min(slots1[ptr1][1], slots2[ptr2][1])
            if min_end - max_start >= duration:
                return [max_start, max_start + duration]
            
            if slots1[ptr1][1] > slots2[ptr2][1]:
                ptr2 += 1
            else:
                ptr1 += 1
            
            
        return []
        
        
        