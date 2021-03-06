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
		self.canvas = SCanvas(self.root)
	
		# INPUT PANEL
		self.inputPanel = InputPanel(self)
		
		self.inputPanel.sailCombobox['values']=("New...")
		self.inputPanel.sailCombobox.current(0)
		
	def changeSail(self, event):
		newSaleName = self.inputPanel.sailCombobox.get();
		if ( (self.model.sail is None) or (newSaleName != self.model.sail.sailName)):
			self.canvas.canvas.delete("all")
			print(event.widget.get())
			if (newSaleName == "New..."):
				self.controller.newSail()
			else:
				self.controller.loadSail(newSaleName)

	def loadSail(self, sail):
		#self.copySailDimensionsToEditBoxes(sail)
		self.inputPanel.setSail(sail)
		