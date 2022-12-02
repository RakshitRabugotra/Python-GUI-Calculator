import tkinter as tk
import src.constants as ct

class Calculator:
    def __init__(self, master: tk.Tk = None):
        """
        """
        # If the master is None, then initialize a new master
        master = tk.Tk() if (master is None) else master

        # Configure the master instance
        master.config(bg=ct.MASTER['bg'])
        master.title(ct.TITLE)
        master.resizable(*ct.RESIZABLE)

        # Making a few TK variables, to use with TK widgets
        self.tkStringVarEntryBox = tk.StringVar(value="0")

        # Set the master as class property
        self.master = master

    def update(self):
        """
            To call the master's .update() method
        """
        self.master.update()
    
    def run(self):
        """
            This function runs the Tkinter instance
            by calling masters' .mainloop() method
        """
        self.__layout()
        self.master.mainloop()

    # This is a private function
    def __layout(self):
        """
            This function contains the layout of all the widgets. Also,
            it is called only once when invoking .run() method of this class
        """
        # Copying the value to new variable, so we don't have to write (self)
        # multiple times
        master = self.master

        # NOTE: We will use CamelCase to name Tkinter Widgets, as the names tend to
        #       get too long to write in snake_case.

        # Create an Entry widget to display the result
        tkEntryBox = tk.Entry(master, textvariable=self.tkStringVarEntryBox, **ct.ENTRY)
        tkEntryBox.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, **ct.ENTRY_PACK)

# This statement will be true if the user is directly running
# this python file
if __name__ == '__main__':

    # You can create an instance of the Calculator
    app = Calculator()
    app.run()