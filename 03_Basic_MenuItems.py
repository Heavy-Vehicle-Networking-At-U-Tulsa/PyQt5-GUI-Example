# Introduction to Python GUIs with PyQt5
# Lesson 02:  Add a Button to Change the label

#Import the necessary libraries
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QLabel,
                             QGridLayout,
                             QPushButton,
                             QAction)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

#Define the main window class that inherits the predifined QMainWindow object.
class MainWindow(QMainWindow):
    # All classes (objects) have an __init__() function that is executed when the 
    # class is instanciated. This runs when an instance of the object is created.
    def __init__(self):
        #The super command makes sure the inhereted class is also initiated. 
        super().__init__()
        #assign a variable to keep track of count
        self.counter_value = 0
        #We call a function to initialize the user interface. 
        self.init_ui()

    # Now define the function that initializes the user interface.
    # all functions within a class need to reference itself.
    def init_ui(self): 
        
        # A simple example of some built in functionality is the status bar.
        self.statusBar().showMessage("Status Bar Line.")
        
        #Build common menu options
        menubar = self.menuBar()
        
        #Grab some free icons from http://ionicons.com/ or similar
        #File Menu Items
        file_menu = menubar.addMenu('&File')
        open_file = QAction(QIcon(r'icons\android-folder.png'), '&Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Load Counter Data')
        open_file.triggered.connect(self.load_data)
        file_menu.addAction(open_file)

        exit_action = QAction(QIcon(r'icons\close-round.png'), '&Exit', self)        
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close) #This is built in
        file_menu.addAction(exit_action)

        #Data Menu Items
        data_menu = menubar.addMenu('&Counter')
        decrement_action = QAction(QIcon(r'icons\minus-round.png'), '&Decrement', self)        
        decrement_action.setStatusTip('Subtract from the running counter')
        decrement_action.triggered.connect(self.decrement_count)
        data_menu.addAction(decrement_action)

        main_toolbar = self.addToolBar("Main")

        main_toolbar.addAction(decrement_action)

        ####
        #Assignment 1: Add an The decrement_count function
        #Assignment 2: Add the increment count menu item
        #Assignment 3: Add the increment count toolbar item
        #Assignment 4: Add the ability to save the count
        ####



        # Let's make a simple label widget to keep track of a count
        self.counter_label = QLabel("Hello PyQt5")
        
        #Make a button that does something.
        #The & symbol adds the ability for the letter after it to be used to click with the Alt key
        # Example: Alt - i does the same as cicking on the button.
        increment_button = QPushButton("&Increment Count",self)
        #connect the triggered signal to the increment_count slot. We have to create that function.
        increment_button.clicked.connect(self.increment_count)

        #Define a main widget that will contain all the other widgets and set
        #it as the central widget. 
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        #A layout manager is needed to put things where we want. Let's use a grid.
        grid_layout = QGridLayout(main_widget)
        #assign the label to the grid.
        grid_layout.addWidget(self.counter_label,0,0,1,1)
        #assign the button to the grid
        grid_layout.addWidget(increment_button,1,0,1,1)

        #Setup the window title and make it appear
        self.setWindowTitle("Lesson 01: Basic Main Window")
        self.show() #This is needed for the window to appear.

    def increment_count(self):
        self.counter_value += 1
        self.counter_label.setText("{}".format(self.counter_value)) 
        print(self.counter_label.text())
    
    def decrement_count(self):
        self.counter_value -= 1
        self.counter_label.setText("{}".format(self.counter_value)) 
        print(self.counter_label.text())
    
    def load_data(self):
        #Write this function
        pass

# This line is run when the to get everything started.      
if __name__ == '__main__':
    app = QApplication([]) #The empty list ([]) is passed inplace of system arguments.
    execute = MainWindow() #Calls the main window class we defined earlier.
    app.exec_() #this starts the event handling loop to accept interaction.