# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        # out of bounds
      
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        # no ships
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # base case of len 1
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1
        
        midX = (bottomLeft.x + topRight.x) // 2
        midY = (bottomLeft.y + topRight.y) // 2
        
        return (self.countShips(sea, Point(midX, midY), bottomLeft)) + (self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)))  + (self.countShips(sea,topRight, Point(midX + 1, midY + 1))) + (self.countShips(sea,Point(topRight.x, midY), Point(midX + 1, bottomLeft.y)))
        
        
        
        
        
        
        