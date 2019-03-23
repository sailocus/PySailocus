'''
@author: Paul DiCarlo
@copyright: 2018, 2019 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''

from pysailocus.geometry.Point import Point
from pysailocus.geometry.Triangle import Triangle
import logging

logger = logging.getLogger('pysailocus')


################################################################
#
################################################################
class Sail(object):

	################################################################
	def __init__(self, tack : Point, clew : Point, head=None, peak=None, throat=None, sailName = None):

		if clew is not None:
			if not isinstance(clew, Point):
				raise Exception("clew must be of type Point or None")
		if head is not None:
			if not isinstance(head, Point):
				raise Exception("head must be of type Point or None")
		if peak is not None:
			if not isinstance(peak, Point):
				raise Exception("peak must be of type Point or None")
		if throat is not None:
			if not isinstance(throat, Point):
				raise Exception("throat must be of type Point or None")


	
		self.sailName = sailName 
		
		params = "tack="+str(tack)+", clew="+str(clew)+", head="+str(head)+", peak="+str(peak)+", throat="+str(throat)
		
		bHead = head is not None
		bPeak = peak is not None
		bThroat = throat is not None
		
		logger.debug('params={0}'.format(params))
		if (bHead and bPeak and bThroat) or (not bHead and not bPeak and not bThroat) :
			raise ValueError('Sail constructor: head, peak, and throat cannot all populated or non empty.  params=' + params)
		if (bPeak and not bThroat) or (not bPeak and bThroat):
			raise ValueError('Sail constructor: If peak or throat is populated, then both must be. params=' + params)
		
		self.peak = peak
		self.throat = throat
		self.tack = tack
		self.clew = clew
		self.head = head
		
		
		self.POINT_NAME_PEAK = "Peak"
		self.POINT_NAME_THROAT = "Throat"
		self.POINT_NAME_TACK = "Tack"
		self.POINT_NAME_CLEW = "Clew"
		self.POINT_NAME_HEAD = "Head"
		
		self.calculateCenterOfEffort()

	################################################################
	def __str__(self):
		return "[peak=" + str(self.peak) + ",throat=" + str(self.throat) + \
			", tack=" + str(self.tack) + ", clew=" + str(self.clew) + ", head=" + str(self.head) +"]"

	################################################################
	# peak throat
	# tack clew
	def validateSail(self):
		numSides = self.getNumSides()
		logger.debug('VALIDATING {0} SIDES'.format(numSides))
		if 4 == numSides:
			if self.peak.y <= self.tack.y or self.peak.y <= self.clew.y:
				raise ValueError("Peak must have y value greater than tack or clew. \n" +str(self) )
		if 3 == numSides:
			if  self.head.y <= self.tack.y or self.head.y <= self.clew.y:
				raise ValueError("Head must have y value greater than tack or clew. \n" +str(self) )
		return


	################################################################
	# Returns the number of sides.  3 it's a triangle.
	# 4 it's a sprit or lug or something like that
	def getNumSides(self):
		if self.head is None:
			return 4
		return 3

	################################################################
	# Get as a vector of X1,Y1,X2,Y2,....,XN,YN  so that it can be provided as an argument
	# to polygon create method.
	def getCoordinatesAsSingleVector(self):
		if (4 == self.getNumSides()):
			vector = []
			vector.append(self.peak.getX())
			vector.append(self.peak.getY())
			vector.append(self.throat.getX())
			vector.append(self.throat.getY())
			vector.append(self.tack.getX())
			vector.append(self.tack.getY())
			vector.append(self.clew.getX())
			vector.append(self.clew.getY())
			return vector
		if (3 == self.getNumSides()):
			vector = []
			vector.append(self.head.getX())
			vector.append(self.head.getY())
			vector.append(self.tack.getX())
			vector.append(self.tack.getY())
			vector.append(self.clew.getX())
			vector.append(self.clew.getY())
			return vector

	################################################################
	def getCoordinateNamesAsVector(self):
		if (4 == self.getNumSides()):
			vector = []
			vector.append(self.POINT_NAME_PEAK)
			vector.append(self.POINT_NAME_THROAT)
			vector.append(self.POINT_NAME_TACK)
			vector.append(self.POINT_NAME_CLEW)
		if (3 == self.getNumSides()):
			vector = []
			vector.append(self.POINT_NAME_HEAD)
			vector.append(self.POINT_NAME_TACK)
			vector.append(self.POINT_NAME_CLEW)
		return vector

	################################################################
	def getComponentTriangles(self):
		componentTriangles = []
		if ( 4 == self.getNumSides()):
			componentTriangles.append(Triangle(self.peak, self.throat, self.clew))
			componentTriangles.append(Triangle(self.throat, self.clew, self.tack))
		else:
			componentTriangles.append(Triangle(self.head, self.clew, self.tack))
		return componentTriangles

	################################################################
	def calculateCenterOfEffort(self):
		logger.debug("TODO:  IMPLEMENT calculateCenterOfEffort()!")
################################################################
#
################################################################
def getSailPointFromJson(pointName, jsonData):
	for sailPoint in jsonData["sail_points"]:
		if (pointName == sailPoint["location"]):
			return Point(sailPoint["coordinates"][0], sailPoint["coordinates"][1])
	return None
	
################################################################
#
################################################################
def createSailFromJson(jsonData):
	sailName = jsonData["sail_name"]
	
	logger.debug('length={0}'.format(len(jsonData["sail_points"])))
	#tack, clew, head=None, peak=None, throat=None):
	
	peak = getSailPointFromJson("peak", jsonData)
	tack = getSailPointFromJson("tack", jsonData)
	clew = getSailPointFromJson("clew", jsonData)
	throat = getSailPointFromJson("throat", jsonData)
	head = getSailPointFromJson("head", jsonData)
	
	sail = Sail(peak=peak, tack=tack, clew=clew, throat=throat, head=head, sailName = sailName)
	return sail
	
	
	

##########################################
# 
# Just for Testing
#
##########################################
if __name__ == "__main__":
	x = Sail(peak=Point(310,400), throat=Point(60,240), tack=Point(10,20), clew = Point(350,15), )
	print(str(x.getNumSides()))
	print(str(x.getCoordinatesAsSingleVector()))
	x = Sail(Point(6,7), Point(7,8), Point(8,9))
	print(str(x.getNumSides()))
	#x = Sail(1, 2, None, None, 5)    

