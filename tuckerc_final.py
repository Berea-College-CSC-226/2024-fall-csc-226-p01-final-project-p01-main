######################################################################
# Author: Caleb Tucker
# Username: tuckerc
#
# P01: Final Project
#
# Purpose: To create an interactive calendar
#######################################################################
# Acknowledgements: Python Documentation, Runestone Academy
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk
from tkinter import messagebox

class CoursePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Planner") # Title
        self.root.geometry("700x400") # Window dimensions
        self.time_slots = [f"{hour}:00" for hour in range(8, 22)]  # Initializes time slots of 8 AM to 9 PM
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # Uses nested loops to create a dictionary for the days of the week
        self.schedule = {day: {time: "" for time in self.time_slots} for day in self.days}
        self.create_calendar()

    def create_calendar(self):
        pass

    def save_schedule(self, day, time, value, event):
        pass

    def display_schedule(self):
        pass
        schedule_display = ""
        messagebox.showinfo("Your Schedule", schedule_display)

root = tk.Tk()
planner = CoursePlanner(root)

root.mainloop()
