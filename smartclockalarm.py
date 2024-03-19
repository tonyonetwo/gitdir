# SmartClock without Alarm is further modifed to the one with an alarm
## add alarm in the GUI clock with strframe in Python
#---------------------------------------------------------------------------------------------------
# modify the previous Tkinter-based smartclock GUI (smartclocknoalarm.py) with an alarm feature. 
## include an option for the user to set an alarm time using a StringVar to track the time input. 
## when the clock matches the alarm time, display a simple popup message as the alarm notification.
#---------------------------------------------------------------------------------------------------
## next consideration 1 : can we pack the smartclockalarm.py into an application that can running in Linux or Windows? 
## next consideration 2 : can we integrate the smartclockalarm.py code into a webpage that can read by the browser Firefox or Chrome?
## implement the above consideration by using the Copilot, Devin or other AIs, which one is the best?
#

import tkinter as tk
from tkinter import simpledialog, messagebox
from time import strftime

class SmartClock:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartClock with Alarm")
        
        # Setting up the window size
        self.root.geometry("400x120")
        self.root.resizable(0, 0)

        # Create a label to display the time
        self.time_label = tk.Label(self.root, font=('calibri', 40, 'bold'),
                                   background='purple', foreground='white')
        self.time_label.pack(anchor='center')

        # Alarm time
        self.alarm_time = tk.StringVar()
        
        # Set Alarm Button
        set_alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm,
                                     font=('calibri', 15, 'bold'), background='orange', foreground='white')
        set_alarm_button.pack(anchor='s')

        self.update_clock()

    def update_clock(self):
        current_time = strftime('%H:%M:%S %p')  # Format the time
        self.time_label.config(text=current_time)  # Update the label with the current time
        if self.alarm_time.get() == strftime('%H:%M'):
            messagebox.showinfo("Alarm", "It's time to take a rest!")
        self.root.after(1000, self.update_clock)  # Call `update_clock` again after 1,000 milliseconds

    def set_alarm(self):
        alarm = simpledialog.askstring("Alarm", "Set alarm time (HH:MM)", parent=self.root)
        if alarm:
            self.alarm_time.set(alarm)
            messagebox.showinfo("Alarm", f"Alarm set for {alarm}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartClock(root)
    root.mainloop()
   
