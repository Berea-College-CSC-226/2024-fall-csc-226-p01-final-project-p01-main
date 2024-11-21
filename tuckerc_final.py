######################################################################
# Author: Caleb Tucker
# Username: tuckerc
#
# P01: Final Project
#
# Purpose: To create an interactive calendar
#######################################################################
# Acknowledgements:
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk
from tkinter import messagebox

class CoursePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Planner")
        self.root.geometry("700x400")

    def create_calendar(self):
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def save_schedule(self, day, time, value, event):

    def display_schedule(self):
        schedule_display = ""
        messagebox.showinfo("Your Schedule", schedule_display)

root = tk.Tk()
planner = CoursePlanner(root)

root.mainloop()
