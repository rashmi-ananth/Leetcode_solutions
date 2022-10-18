class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        coordinates.sort()
        if len(coordinates) == 2:
            return True
        if len(coordinates) < 2:
            return False
        
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        
        for i in range(len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            
            if dx * (y-y1) != dy * (x-x1):
                return False
            
        return True
            
            
        

            
            
        return True
 
            
        