'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''

from pysailocus.sail.Sail import Sail
from pysailocus.geometry.Line import Line, intersection
from pysailocus.geometry.Point import Point
from pysailocus.geometry.Triangle import Triangle
from pysailocus.geometry.LineSegment import LineSegment
from pysailocus.geometry.LineSegment import getPerpendicularLineSegmentPoint

################################################################
#
################################################################
class CenterOfEffort(object):
	
	################################################################
	def __init__(self, sail):
		
		self.sail = sail;
		#self.sail.validateSail()
		
		
		###### KEY MEMBER ATTRIBUTES *******
		self.center_of_effort : Point = None
		self.component_centers_of_effort = []
		self.centroid_line_segments = []
		self.lines_perpendicular_to_centroid_line_segments = []
		self.lines_connecting_centroid_line_segments = []
		###### KEY MEMBER ATTRIBUTES *******
		
		
		# OK... Now get the 
		for triangle in sail.getComponentTriangles():
			for lineSegment in triangle.getCentroidLineSegments():
				self.centroid_line_segments.append(LineSegment(lineSegment.point_a, lineSegment.point_b))
			
			center_of_effort = triangle.getCentroidPoint()

			self.component_centers_of_effort.append(center_of_effort)
			print("new center_of_effort: {0}   size={1}".format(center_of_effort, len(self.component_centers_of_effort)))
			
		for i in self.component_centers_of_effort:
			print("\t center_of_effort is " + str(i))	
			
				
		if len(self.component_centers_of_effort) > 1: 
			print("a={0} b={0}".format(self.component_centers_of_effort[0],self.component_centers_of_effort[1]))
			self.lines_connecting_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[0], self.component_centers_of_effort[1]))
		else:
			self.center_of_effort = self.component_centers_of_effort[0]
			return # 3 pointed sail, so easy, we are done and can return


		triangleArea1 =  Triangle(self.sail.throat,self.sail.clew,self.sail.peak).area()
		triangleArea2 = Triangle(self.sail.throat, self.sail.clew, self.sail.tack).area()
		print("triangleArea1={0}  triangleArea2={1}".format(triangleArea1, triangleArea2))
		
		
		tp1 = getPerpendicularLineSegmentPoint(self.component_centers_of_effort[0], self.component_centers_of_effort[1], int(triangleArea2/1000))
		self.lines_perpendicular_to_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[0], tp1))
		tp2 = getPerpendicularLineSegmentPoint(self.component_centers_of_effort[1], self.component_centers_of_effort[0], int(-1*triangleArea1/1000))
		self.lines_perpendicular_to_centroid_line_segments.append(LineSegment(self.component_centers_of_effort[1], tp2))
		
		self.tp_lineSegment = LineSegment(tp1, tp2)


		line1 = Line(self.lines_connecting_centroid_line_segments[0].point_a, self.lines_connecting_centroid_line_segments[0].point_b)
		line2 = Line(tp1, tp2)
		
		self.center_of_effort = intersection(line1, line2)
		

################################################################
# M A I N 
################################################################
if __name__ == "__main__":		
	print("")
	sail = Sail(peak=Point(310,400), throat=Point(60,240), tack=Point(10,20), clew = Point(350,15), )
	coe = CenterOfEffort(sail)
		
