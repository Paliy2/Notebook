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
    notebook.new_note('Hello Oles')
    # class variable, like self,var
    print(isinstance(notebook.notes, list))
    # representing an object
    print(str(notebook))
    
    
