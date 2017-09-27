# Introduction to Python GUIs with PyQt5
# Lesson 01:  Basic main window

#Import the necessary libraries
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QLabel,
                             QGridLayout)
from PyQt5.QtCore import QCoreApplication

#Define the main window class that inherits the predifined QMainWindow object.
class MainWindow(QMainWindow):
    # All classes (objects) have an __init__() function that is executed when the 
    # class is instanciated. This runs when an instance of the object is created.
    def __init__(self):
        #The super command makes sure the inhereted class is also initiated. 
        super().__init__()
        #We call a function to initialize the user interface. 
        self.init_ui()
        
    # Now define the function that initializes the user interface.
    # all functions within a class need to reference itself.
    def init_ui(self): 
        
        # A simple example of some built in functionality is the status bar.
        self.statusBar().showMessage("Status Bar Line.")
        
        # Let's make a simple label widget. We have to be sure to have this imported.
        greeting_label = QLabel("Hello PyQt5")
        
        #Define a main widget that will contain all the other widgets and set
        #it as the central widget. 
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        #A layout manager is needed to put things where we want. Let's use a grid.
        grid_layout = QGridLayout(main_widget)
        #assign the label to the grid.
        grid_layout.addWidget(greeting_label,0,0,1,1)

        #Setup the window title and make it appear
        self.setWindowTitle("Lesson 01: Basic Main Window")
        self.show() #This is needed for the window to appear.

# This line is run when the to get everything started.      
if __name__ == '__main__':
    app = QApplication([]) #The empty list ([]) is passed inplace of system arguments.
    execute = MainWindow() #Calls the main window class we defined earlier.
    app.exec_() #this starts the event handling loop to accept interaction.