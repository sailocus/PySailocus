'''
@author: Paul DiCarlo
@copyright: 2018, 2019 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
from tkinter import *
from tkinter import ttk
from pysailocus.geometry.Point import Point 
from pysailocus.sail.Sail import Sail
from pysailocus.sail.CenterOfEffort import CenterOfEffort

####################################################
#
####################################################
class SCanvas(object):

	####################################################
	def invert_x_coordinate(self, sail): 
		
		self.canvas.update()
		height = self.canvas.winfo_height()
		
		
		
		if 4 == sail.getNumSides():
			transformedSail = Sail(
				peak=Point(sail.peak.getX(), height - sail.peak.getY()),
				throat=Point(sail.throat.getX(), height - sail.throat.getY()),
				tack=Point(sail.tack.getX(), height - sail.tack.getY()),
				clew=Point(sail.clew.getX(), height - sail.clew.getY())
			)
		if 3 == sail.getNumSides():
			transformedSail = Sail(
				head=Point(sail.head.getX(), height - sail.head.getY()),
				tack=Point(sail.tack.getX(), height - sail.tack.getY()),
				clew=Point(sail.clew.getX(), height - sail.clew.getY())
			)
			
		return transformedSail

	####################################################
	def drawLine(self, p1, p2, fill):
		self.canvas.create_line(
			p1.getX(),
			p1.getY(),
			p2.getX(),
			p2.getY(), fill=fill)


	####################################################
	def drawSail(self, sail):
		
		self.canvas.delete("all")

		transformedSail = self.invert_x_coordinate(sail)
		
		
		
		coordinates = transformedSail.getCoordinatesAsSingleVector()
		names = transformedSail.getCoordinateNamesAsVector()
		self.canvas.create_polygon(coordinates, fill='wheat2')
		
		for x in range(0, int(len(coordinates)/2)):
			self.canvas.create_oval(
				coordinates[x*2]-3, 
				coordinates[x*2+1]-3,
				coordinates[x*2]+3, 
				coordinates[x*2+1]+3,
				fill='black')

			self.canvas.create_text(
				coordinates[x*2]+25,
				coordinates[x*2+1]-10,
				fill="darkblue",font="Helvetica 10",
				text=names[x])

		if sail.getNumSides() > 3:
			#draw line from throat to clew
			self.canvas.create_line(
				transformedSail.throat.getX(),
				transformedSail.throat.getY(),
				transformedSail.clew.getX(),
				transformedSail.clew.getY(),dash=(4, 2))
		
		
		#-------------------------------------------------
		# Create CenterOfEffort object and draw to canvas
		#-------------------------------------------------
		self.drawCenterOfEffort(transformedSail)
	
	##############################################################################
	def drawCenterOfEffort(self, transformedSail):
		coe = CenterOfEffort(transformedSail)
		for cls in coe.centroid_line_segments:
			self.drawLine(cls.point_a, cls.point_b, "White")
			
		for coePoint in coe.component_centers_of_effort:
			self.canvas.create_oval(
                coePoint.getX()-1, 
                coePoint.getY()-1,
                coePoint.getX()+1, 
                coePoint.getY()+1,
                fill='black')
			
		for coeLineSegment in coe.lines_connecting_centroid_line_segments:
			self.drawLine(coeLineSegment.point_a , coeLineSegment.point_b, fill='Red')
			
		for lspcls in coe.lines_perpendicular_to_centroid_line_segments:
			self.drawLine(lspcls.point_a , lspcls.point_b, fill='Purple')
			
			
		self.drawLine(coe.tp_lineSegment.point_a, coe.tp_lineSegment.point_b, fill="blue2")
		
		# and finally draw the center of effort
		pxSize = 4
		self.canvas.create_oval(
                coe.center_of_effort.getX()-pxSize, 
                coe.center_of_effort.getY()-pxSize,
                coe.center_of_effort.getX()+pxSize, 
                coe.center_of_effort.getY()+pxSize,
                fill='black')
		
		
		coe_string='COE=({0},{1})'.format(coe.center_of_effort.getX(), coe.center_of_effort.getY())
		
		self.canvas.create_text(
				coe.center_of_effort.getX()+25,
				coe.center_of_effort.getY()-10,
				fill="darkblue",font="Helvetica 10",
				text=coe_string)
		
			
	###########################################################
	def __init__(self, parentWindow):
		frameWindow = ttk.Frame(parentWindow, padding="3 3 12 12 ", relief="sunken", width=200, height=200)
		frameWindow.grid(column=1, row=0, columnspan=1, rowspan=5, sticky=N+S+E+W)
		frameWindow.grid_configure(padx=5, pady=5)
		
		
		self.frameWindow = frameWindow
		
		self.canvas = Canvas(frameWindow, bg='white')
		self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)
