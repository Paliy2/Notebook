import sys
from notebook import Note, Notebook
from menu import Menu

if __name__ == '__main__':
    print(dir(Notebook))  # methods
    print(dir(Note))  # methods
    print(dir(Menu))  # methods

    # object of the class
    notebook = Notebook()
    # method in use
    notebook.new_note('Hello Oles')
    # class 
    print(isinstance(notebook.notes, list))
