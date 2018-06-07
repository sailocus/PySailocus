'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''


################################################################
# class Point corresponds to the x,y coordinates of the corners 
# of a 3 or 4 sided sail (Tack, Clew, Head, Peak, and Throat)
################################################################
class Point(object):

	################################################################
	def __init__(self, x, y):
		self.x = int(x) 
		self.y = int(y) 

	################################################################   
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"

	################################################################
	def getX(self):
		return self.x

	################################################################
	def getY(self):
		return self.y

	################################################################
	def isEqual(self, some_point):
		if (self.x != some_point.x):
			return False
		if (self.y != some_point.y):
			return False
		return True