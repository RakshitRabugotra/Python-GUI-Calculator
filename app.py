import tkinter as tk
import src.constants as ct

class Calculator:
    def __init__(self, master: tk.Tk = None):
        """
        """
        # Configure the master instance
        master.config(bg=ct.MASTER['bg'])
        master.title(ct.TITLE)
        master.resizable(*ct.RESIZABLE)

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
        self.master.mainloop()


# This statement will be true if the user is directly running
# this python file
if __name__ == '__main__':
    # You can create an instance of the Calculator
    app = Calculator()
    app.run()
