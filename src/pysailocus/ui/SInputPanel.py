'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
from tkinter import *
from tkinter import ttk
from pysailocus.sail.Sail import Sail
from pysailocus.geometry.Point import Point



class InputPanel(object):
    '''
    classdocs
    '''
    def __init__(self, parentWindow, canvasWindow):
        '''
        Constructor
        '''
        self.parentWindow = parentWindow
        self.canvasWindow = canvasWindow
        
        # We'll have a frame in a frame.  Top level frame will
        # be resizable on all sides
        topFrame = ttk.Frame(parentWindow, padding="3 3 12 12 ")
        topFrame.grid(column=0, row=0, sticky=N+S+E+W)
        topFrame.columnconfigure(0, weight=1)
        topFrame.rowconfigure(0, weight=1)
        
        
        # Now the frame window the input widgets go into
        frameWindow = ttk.Frame(topFrame, padding="3 3 12 12 ")
        frameWindow.grid(column=0, row=0, sticky=(N, W))
        frameWindow.columnconfigure(0, weight=1)
        frameWindow.rowconfigure(0, weight=1)
        
        self.pointNames=['Peak','Throat','Tack','Clew']
        
        self.head_x = StringVar()
        self.head_y = StringVar()
        self.peak_x = StringVar()
        self.peak_y = StringVar()
        self.throat_x = StringVar()
        self.throat_y = StringVar()
        self.tack_x = StringVar()
        self.tack_y = StringVar()
        self.clew_x = StringVar()
        self.clew_y = StringVar()

        ######################
        # LABELS
        ######################        
        my_row=1;
        my_column=2;
        ttk.Label(frameWindow, text="X coord").grid(column=my_column, row=my_row);
        my_column=my_column+1; 
        ttk.Label(frameWindow, text="Y coord").grid(column=my_column, row=my_row); 
        
        my_column=1
        my_row=my_row+1;
        ttk.Label(frameWindow, text="Head").grid(column=my_column, row=my_row);
        my_row=my_row+1;
        ttk.Label(frameWindow, text="Peak").grid(column=my_column, row=my_row); 
        my_row=my_row+1
        ttk.Label(frameWindow, text="Throat").grid(column=my_column, row=my_row); 
        my_row=my_row+1
        ttk.Label(frameWindow, text="Tack").grid(column=my_column, row=my_row); 
        my_row=my_row+1
        ttk.Label(frameWindow, text="Clew").grid(column=my_column, row=my_row); 
        
        
        ######################
        # ENTRY BOXES
        ######################
        my_row=2
        my_col=2
        self.head_entry_x = ttk.Entry(frameWindow, width=7, textvariable=self.head_x); 
        self.head_entry_x.grid(column=my_col, row=my_row, sticky=(W,E))
        my_col = my_col+1
        self.head_entry_y = ttk.Entry(frameWindow, width=7, textvariable=self.head_y)
        self.head_entry_y.grid(column=my_col, row=my_row, sticky=(W,E))
        #TODO:  Get 3 sided sail working
        self.head_entry_x.config(state=DISABLED) #<---- #TODO:  Get 3 sided sail working
        self.head_entry_y.config(state=DISABLED) #<---- #TODO:  Get 3 sided sail working
        
        my_row=my_row+1
        my_col=2
        self.peak_entry_x = ttk.Entry(frameWindow, width=7, textvariable=self.peak_x); 
        self.peak_entry_x.grid(column=my_col, row=my_row, sticky=(W,E))
        my_col = my_col+1
        self.peak_entry_y = ttk.Entry(frameWindow, width=7, textvariable=self.peak_y)
        self.peak_entry_y.grid(column=my_col, row=my_row, sticky=(W,E))
        
        my_row=my_row+1
        my_col=2
        self.throat_entry_x = ttk.Entry(frameWindow, width=7, textvariable=self.throat_x)
        self.throat_entry_x.grid(column=my_col, row=my_row, sticky=(W,E)); 
        my_col = my_col+1
        self.throat_entry_y = ttk.Entry(frameWindow, width=7, textvariable=self.throat_y)
        self.throat_entry_y.grid(column=my_col, row=my_row, sticky=(W,E))
        
        my_row=my_row+1
        my_col=2
        self.tack_entry_x = ttk.Entry(frameWindow, width=7, textvariable=self.tack_x)
        self.tack_entry_x.grid(column=my_col, row=my_row, sticky=(W,E)); 
        my_col = my_col+1
        self.tack_entry_y = ttk.Entry(frameWindow, width=7, textvariable=self.tack_y)
        self.tack_entry_y.grid(column=my_col, row=my_row, sticky=(W,E))
        
        my_row=my_row+1
        my_col=2
        self.clew_entry_x = ttk.Entry(frameWindow, width=7, textvariable=self.clew_x)
        self.clew_entry_x.grid(column=my_col, row=my_row, sticky=(W,E)); 
        my_col = my_col+1
        self.clew_entry_y = ttk.Entry(frameWindow, width=7, textvariable=self.clew_y)
        self.clew_entry_y.grid(column=my_col, row=my_row, sticky=(W,E))
        
        self.entryList = [
            self.head_entry_x,
            self.head_entry_y,
            self.peak_entry_x,
            self.peak_entry_y,
            self.throat_entry_x,
            self.throat_entry_y,
            self.tack_entry_x, 
            self.tack_entry_y,
            self.clew_entry_x,
            self.clew_entry_y
            ]
        
        self.entryDisEnablement = [
            [
                self.peak_entry_x,
                self.peak_entry_y,
                self.throat_entry_x,
                self.throat_entry_y,
                ],[
                self.head_entry_x,
                self.head_entry_y
                ]
            ]
        
        
        ####################################
        # RADIO BUTTONS
        ####################################
        my_col=2
        self.sailSides = IntVar()
        my_row=my_row+1
        self.button_3sides= Radiobutton(frameWindow, text="3 sided sail", variable=self.sailSides, value=0,command=self.radioButtonSelected)
        self.button_3sides.grid(column=my_col, row=my_row, columnspan=2)
        self.button_3sides.deselect()
        my_row=my_row+1
        self.button_4sides=Radiobutton(frameWindow, text="4 sided sail", variable=self.sailSides, value=1, command=self.radioButtonSelected)
        self.button_4sides.grid(column=my_col, row=my_row, columnspan=2)
        self.button_4sides.select() #<--- #TODO:  add 3 sided sails
        
        
        self.button_3sides.config(state=DISABLED) #<---- #TODO:  Get 3 sided sail working
        
        
        #######################
        # CALCULATE BUTTON
        #######################
        my_row=my_row+1
        self.button_calc = ttk.Button(frameWindow, text="Calculate", command=self.calculate)
        self.button_calc.grid(column=2, row=my_row, sticky=(E,W), columnspan=2)
        self.radioButtonSelected()
        
        for child in frameWindow.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
   
    '''
    The Tkinter canvas has the y=0 at the top of the window, but we prefer the  bottom.
    '''
    def invert_x_coordinates(self, coordinates): 
        
        self.canvasWindow.canvas.update()
        height = self.canvasWindow.canvas.winfo_height()
    
        retVal=[]
        idx=0
        for x in coordinates:
            a = x
            if (idx % 2) == 1: # if is odd
                a = height - a # then this is the y param, adjust for axis on bottom
            retVal.append(a)
            idx=idx+1 # increment index
            
        return retVal
                
            
    def calculate(self, *args):
        '''
        try:
           
            coordinates = []          
            for x in self.coordinates:
                if not x.get().isdigit():
                    messagebox.showinfo("Coordinate Problem", "Not a digit!" + x.get())
                    return
                coordinates.append(int(x.get()))
            
        except ValueError:
            pass
        
 
        '''
        
        #corrected_coords = self.invert_x_coordinates(self.editBoxesToSail().getCoordinatesAsSingleVector() )
        sail = self.editBoxesToSail()
        
        try:
            sail.validateSail()
        except ValueError as e:
            messagebox.showerror("Error on coordinates", str(e))
            self.canvasWindow.canvas.delete("all")
            raise
        
        self.canvasWindow.drawSail(sail)



      
    '''
    #TODO: Need to get this out of the ui and into the controller
    Take contents from Edit box and create a sail definition.
    '''  
    def editBoxesToSail(self):
        try:
            return Sail(
                peak=Point(int(self.peak_x.get()), int(self.peak_y.get())),
                throat=Point(int(self.throat_x.get()), int(self.throat_y.get())),
                tack=Point(int(self.tack_x.get()), int(self.tack_y.get())),
                clew=Point(int(self.clew_x.get()), int(self.clew_y.get())))
        except ValueError as e:
            messagebox.showerror("Error on coordinates", str(e))
            raise
        
            
    '''
    Copy sail dimension for a Sail object to the edit boxes on the panel.
    '''
    def copySailDimensionsToEditBoxes(self, sailDimensions): 
        self.peak_x.set(sailDimensions.peak.getX())
        self.peak_y.set(sailDimensions.peak.getY())
        self.throat_x.set(sailDimensions.throat.getX())
        self.throat_y.set(sailDimensions.throat.getY())
        self.tack_x.set(sailDimensions.tack.getX())
        self.tack_y.set(sailDimensions.tack.getY())
        self.clew_x.set(sailDimensions.clew.getX())
        self.clew_y.set(sailDimensions.clew.getY())
        
    def radioButtonSelected(self):
      
        # Reset all text boxes to enabled
        for b in self.entryList:
            b.config(state=NORMAL)
        
        # Now disable text boxes not needed for the chosen number of sides.   
        for b in self.entryDisEnablement[self.sailSides.get()]:
            b.config(state=DISABLED)   
     
            