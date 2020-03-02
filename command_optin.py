import sys
from notebook import Note, Notebook
from menu import Menu

if __name__ == '__main__':
    print(dir(Notebook))  # methods
    print(dir(Note))  # methods
    print(dir(Menu))  # methods

    # object of the class
    # calling __init__ while creating
    notebook = Notebook()
    # method in use
    # self represents the instance of the class. 
    # self is the parameter of class
    # we can access it by using self.var. Instead of self here should be the name of object
    notebook.new_note('Hello Oles')
    # class function variable, like self,var
    print(isinstance(notebook.notes, list))
    # representing an object
    print(str(notebook))
    
    
