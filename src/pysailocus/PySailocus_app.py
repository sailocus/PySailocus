'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''

from pysailocus.SController import Controller

import logging
import sys




#########################################################
# M A I N 
#########################################################
if __name__ == "__main__":
    logger = logging.getLogger('pysailocus')
    logger.setLevel(logging.DEBUG)
    
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    
    #c = COEApp();
    controller = Controller()