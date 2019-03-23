'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''

from pysailocus.geometry.Line import Line 
from pysailocus.geometry.LineSegment import LineSegment
from pysailocus.geometry.Line import intersection
from pysailocus.geometry.Point import Point



################################################################
#
################################################################
class Triangle(object):
	
	################################################################
	def __init__(self, point_a : Point, point_b : Point, point_c : Point):
		self.point_a = point_a
		self.point_b = point_b
		self.point_c = point_c

		self.validate()
	
	################################################################		
	def validate(self):
		if self.point_a is None or self.point_b is None or self.point_c is None:
			raise ValueError("Triangle: none of 3 points may be None: " + str(self))
		
		if not isinstance(self.point_a, Point) or not isinstance(self.point_b, Point) or not isinstance(self.point_b, Point):
			raise ValueError("Triangle: all args must be of type Point")
		
		if self.point_a.isIdentical(self.point_b) or self.point_a.isIdentical(self.point_c) or self.point_b.isIdentical(self.point_c):
			raise ValueError("Triangle: All 3 points of the triangle must be unique of each other.")
			
	def __str__(self):
		return "Triangle=[a=" + str(self.point_a) + ", b=" + str(self.point_b) + ", c=" + str(self.point_c) + "]"
	
	################################################################
	# Gets area of triangle.
	def area(self):
		self.validate()
		
		area = abs(   (  self.point_a.x*(self.point_b.y-self.point_c.y)  +  self.point_b.x*(self.point_c.y-self.point_a.y)  
						+  self.point_c.x*(self.point_a.y-self.point_b.y) )/2     )
		return area
	
	################################################################
	def getCentroidLineSegments(self):
		self.validate()
		
		lineSegments = []
		
		midpoint_c = LineSegment(self.point_a, self.point_b).getMidpoint()
		lineSegments.append(LineSegment(midpoint_c, self.point_c))
		
		midpoint_b = LineSegment(self.point_a, self.point_c).getMidpoint()
		lineSegments.append(LineSegment(midpoint_b, self.point_b))
		
		midpoint_a = LineSegment(self.point_b, self.point_c).getMidpoint()
		lineSegments.append(LineSegment(midpoint_a, self.point_a))
		
		return lineSegments
	
	################################################################
	def getCentroidPoint(self):
		self.validate()
		
		# the centroid is the intersection of the centroid line segments.
		lineSegments = self.getCentroidLineSegments()
		
		l1 = Line(lineSegments[0].point_a, lineSegments[0].point_b)
		l2 = Line(lineSegments[1].point_a, lineSegments[1].point_b)
		
		coe = intersection(l1, l2)
		
		
		return coe
	
	
################################################################
# M A I N
################################################################	
if __name__ == "__main__":
	
	t = Triangle(Point(0,0), Point(10,0), Point(5,5))
	print("Area of triangle " + str(t) + " is " + str(t.area()))
	print("Line segmetns of " + str(t) + " is ==> ")
	for segment in t.getCentroidLineSegments():
		print("\t" + str(segment))
	
