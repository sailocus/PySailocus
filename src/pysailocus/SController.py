'''
@author: Paul DiCarlo
@copyright: 2018, 2019 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
import os
from tkinter import Tk
from pysailocus.SModel import SModel
from pysailocus.SView import SView


#########################################################
# MVC class for the controller
#########################################################
class Controller(object):
	
		#################################################
		def __init__(self):
			self.baseTitle = "PySailocus - Python, Tkinter, & Forces on a Sail"
			
			# Create the root window
			self.root = Tk()
			self.root.title(self.baseTitle);
	
			###########################################################
			# MVC...I'm the controller so now for the Model and View...
			###########################################################
			
			# M O D E L
			self.model = SModel(self)
			
			# V I E W
			self.view = SView(self, self.model);

			# Kick things off with the trusty optimist sail
			self.loadSail("Optimist")
			
			############
			# MAIN LOOP 
			############
			self.root.mainloop()
			
			
		'''
		@todo: NOt implemented yet!!!
		'''
		def newSail(self):
			self.model.sail = None
			self.view.inputPanel.clearEditBoxes()
			
			
		def loadSail(self, newSailName):

			self.model.loadSailFromJson(os.path.join(os.path.dirname(__file__),"resources", "models", newSailName + ".json")); 
			self.root.title(self.baseTitle + " - " + str(self.model.getSailName()))
			self.view.loadSail(self.model.sail)
			
		
	
