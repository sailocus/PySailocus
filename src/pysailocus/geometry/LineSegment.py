'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''

from pysailocus.geometry.Point import Point
from pysailocus.geometry.Line import newPointOnLine, getSlope


#############################################################################################
# For pointA, return a point weighed perpendicular to the linesegement as defined by pointb
#############################################################################################
def getPerpendicularLineSegmentPoint(pointA, pointB, weight):
		print("__________________________________________________")
		theSlope = getSlope(pointA, pointB)
		#y_offset = -1* COE.COEMath.getOffsetForY(center_of_effort_1, center_of_effort_2)
		perpendicularSlope = float(-1/theSlope)
		x = pointA.getX()+weight
		newPoint = newPointOnLine( perpendicularSlope, x, pointA )
		if True:
			print("==>original slope=" + str(theSlope))
			#print("==>perpendicular slope=" + str(perpendicularSlope))
			#print("==>calculated y=" + str(y))
			print(str(pointA))
			print(str(pointB))
			print("x=" + str(x))
		#self.drawLine(center_of_effort_1, Point(center_of_effort_1.getX()+24, y), fill='Orange')
		#newPoint = Point(x, y) # create new point to create perpendicular line of weight based on surface area


		return newPoint

################################################################
#
################################################################
class LineSegment(object):
	
	################################################################
	def __init__(self, point_a, point_b):
		
		if not isinstance(point_a, Point):
			raise ValueError("point_a is not a point: " + str(point_a))
		if not isinstance(point_b, Point):
			raise ValueError("point_b is not a point: " + str(point_b))
		
		self.point_a = point_a
		self.point_b = point_b
		
		self.validate()
		
	################################################################
	def __str__(self):
		return "LineSegement=[" + str(self.point_a) + ", " + str(self.point_b) + "]"
		
	################################################################
	def validate(self):
		if self.point_a is None or self.point_b is None:
			raise ValueError("LineSegement: both points must be non-null.  " + str(self))
	
	################################################################	
	def getMidpoint(self):
		self.validate()
		
		return Point(int((self.point_a.x+self.point_b.x)/2), int((self.point_a.y+self.point_b.y)/2))  
	
	
################################################################
# M A I N 
################################################################	
if __name__ == "__main__":
	print(str(LineSegment(Point(0,2), Point(0,4)).getMidpoint().isEqual(Point(0,3))))
	#assert(  False == LineSegment(Point(0,2), Point(0,4)).getMidpoint().isEqual(Point(0,3))), print("Yahoo")
	