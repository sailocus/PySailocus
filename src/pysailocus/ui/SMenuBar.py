'''
@author: Paul DiCarlo
@copyright: 2018 Paul DiCarlo
@license: MIT
@contact: https://github.com/sailocus/PySailocus
'''
from tkinter import Menu
from tkinter import messagebox


class MenuBar(object):
    '''
    classdocs
    '''
    def __aboutHandler(self):
        messagebox.showinfo("PySailocus - Forces on a Sail", "PySailocus is a sail analysis tool written in Python and Tkinter\n\nhttps://github.com/sailocus")


    def __init__(self, parentWindow):
        '''
        Constructor
        '''
        menubar=Menu(parentWindow)
        parentWindow['menu']=menubar
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menu_help = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label="File")
        menubar.add_cascade(menu=menu_edit, label="Edit")
        menubar.add_cascade(menu=menu_help, label="Help")
        
        menu_help.add_command(label='About', command=self.__aboutHandler)