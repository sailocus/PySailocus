'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
import json
from pysailocus.sail.Sail import Sail, createSailFromJson

################################################################
# MVC class for the Model
################################################################
class SModel(object):
	
	################################################################
	def __init__(self, controller):
		
		self.sail = None # gets set by loadSailJson

		
		
	################################################################
	# 	Loads sail from JSON file.
	def loadSailFromJson(self, jsonFile):
		json_jsonData=open(jsonFile).read()
		jsonData = json.loads(json_jsonData)
		self.sail = createSailFromJson(jsonData)
		
		
	################################################################
	def getSailName(self):
		return self.sail.sailName