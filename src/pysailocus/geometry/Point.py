'''
@author: Paul DiCarlo
@copyright: 2018, 2019 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''


################################################################
# class Point corresponds to the x,y coordinates of the corners 
# of a 3 or 4 sided sail (Tack, Clew, Head, Peak, and Throat)
################################################################
class Point(object):

	################################################################
	def __init__(self, x: int, y:int):
		self.x = x
		self.y = y 

	################################################################   
	def __str__(self):
		return '({0},{1})'.format(self.x, self.y)

	################################################################
	def getX(self):
		return self.x

	################################################################
	def getY(self):
		return self.y

	################################################################
	def isIdentical(self, some_point):
		assert isinstance(some_point, Point)
		if (self.x != some_point.x):
			return False
		if (self.y != some_point.y):
			return False
		return True
