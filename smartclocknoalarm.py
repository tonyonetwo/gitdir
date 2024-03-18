# Write a smart clock program in GUI with Python 3 through the use of AI coding assistant LMsys 
# Use python 3 to create a smart alarm clock with Tkinter for GUI creation

import tkinter as tk
from time import strftime

class SmartClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        
        # Setting up the window size
        self.root.geometry("400x200")
        # Making the window not resizable
        self.root.resizable(0, 0)  

        # Create a label to display the time
        self.time_label = tk.Label(self.root, font=('calibri', 40, 'bold'),
                                   background='purple', foreground='white')
        self.time_label.pack(anchor='center')
        
        # Call the `time` method to display the time
        self.update_clock()

    def update_clock(self):
        current_time = strftime('%H:%M:%S %p')  # Format the time
        self.time_label.config(text=current_time)  # Update the label with the current time
        self.root.after(1000, self.update_clock)  # Call `update_clock` again after 1,000 milliseconds

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartClock(root)
    root.mainloop()
