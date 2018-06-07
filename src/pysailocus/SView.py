'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
from pysailocus.SModel import SModel
from pysailocus.ui.SInputPanel import InputPanel
from pysailocus.ui.SMenuBar import MenuBar
from pysailocus.ui.SCanvas import SCanvas
from tkinter import Grid


################################################################
# MVC class for View
################################################################
class SView(object):
	
	################################################################
	def __init__(self, controller, model):
		self.controller = controller
		self.model = model
		
		self.controller = controller
		self.model = model
		self.root = controller.root
		
		Grid.rowconfigure(self.root, 0, weight=1)
		Grid.columnconfigure(self.root, 1, weight=1)  
		self.root.minsize(width=800, height=600)
		self.root.maxsize(width=800, height=600)
		self.root.resizable(False,False)	 
	
		# MENU BAR
		self.menuBar = MenuBar(self.root)
	
		# CANVAS
		self.scanvas = SCanvas(self.root)
	
		# INPUT PANEL
		self.inputPanel = InputPanel(self.root, self.scanvas)
		
		
		
	################################################################	
	def copySailDimensionsToEditBoxes(self, sail):
		self.inputPanel.copySailDimensionsToEditBoxes(sail)