import tkinter as tk
from tkinter import ttk, messagebox

class BusynessManager:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.root = tk.Tk()
        self.root.title("Berea Busy-ness Manager")
        self.setup_input_frame()
        self.setup_calendar_frame()
        self.day_columns = {day: i + 1 for i, day in enumerate(self.days)}
        # Initializes the program
        self.root.mainloop()

    def setup_input_frame(self):
        """Creates the input frame for adding classes."""
        input_frame = ttk.LabelFrame(self.root, text="Add Class")
        input_frame.pack(fill="x", padx=10, pady=5)

        # Allows class name input
        ttk.Label(input_frame, text="Class Name:").grid(row=0, column=0, padx=5, pady=5)
        self.class_name_entry = ttk.Entry(input_frame)
        self.class_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Allows start time input
        ttk.Label(input_frame, text="Start Time (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.start_time_entry = ttk.Entry(input_frame)
        self.start_time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Allows end time input
        ttk.Label(input_frame, text="End Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
        self.end_time_entry = ttk.Entry(input_frame)
        self.end_time_entry.grid(row=2, column=1, padx=5, pady=5)

        # Allows selection of days
        ttk.Label(input_frame, text="Days:").grid(row=3, column=0, padx=5, pady=5)
        self.day_vars = [tk.StringVar() for _ in self.days]
        num_days = len(self.days)
        for i, day in enumerate(self.days):
            ttk.Checkbutton(input_frame, text=day, variable=self.day_vars[i], onvalue=day, offvalue="").grid(
                row=3, column=i + 1, padx=2, pady=2, sticky="w"
            )

        # Ensure the columns are evenly distributed
        for i in range(num_days):
            input_frame.grid_columnconfigure(i + 1, weight=1, uniform="equal")

        add_button = ttk.Button(input_frame, text="Add Class", command=self.add_class)
        add_button.grid(row=4, column=0, columnspan=len(self.days) + 1, pady=10)

    def setup_calendar_frame(self):
        """Creates the calendar frame for displaying classes."""
        calendar_container = ttk.Frame(self.root)
        calendar_container.pack(fill="both", expand=True, padx=10, pady=5)

        # Scrollbar is very important for the program to work
        canvas = tk.Canvas(calendar_container)
        scrollbar = ttk.Scrollbar(calendar_container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Calendar Headers
        for i, day in enumerate(["Time"] + self.days):
            header = ttk.Label(self.scrollable_frame, text=day, anchor="center", relief="ridge")
            header.grid(row=0, column=i, sticky="nsew")

        # Calendar Times
        for i in range(24 * 6):
            time_label = tk.Label(self.scrollable_frame, text=f"{i // 6:02}:{(i % 6) * 10:02}", anchor="e", relief="ridge")
            time_label.grid(row=i + 1, column=0, sticky="nsew")

        # Sets up grid layout
        self.scrollable_frame.columnconfigure(0, weight=1)
        for i in range(1, len(self.days) + 1):
            self.scrollable_frame.columnconfigure(i, weight=1)

    def add_class(self):
        """Allows adding a class through GUI."""
        class_name = self.class_name_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()
        selected_days = [day_var.get() for day_var in self.day_vars if day_var.get()]

        # Ensures all fields are filled
        if not class_name or not start_time or not end_time or not selected_days:
            messagebox.showwarning("Missing Info", "Please fill out all fields. I can't read your mind!")
            return

        # Ensures time format is correct
        try:
            start_hour, start_minute = map(int, start_time.split(":"))
            end_hour, end_minute = map(int, end_time.split(":"))
            assert 0 <= start_hour <= 23 and 0 <= start_minute <= 59
            assert 0 <= end_hour <= 23 and 0 <= end_minute <= 59
        except (ValueError, AssertionError):
            messagebox.showerror("Invalid Format", "Please enter time in 24 hour format HH:MM. No, it's not military time.")
            return

        # Display the class in the calendar
        for day in selected_days:
            day_column = self.day_columns[day]
            class_label = tk.Label(self.scrollable_frame, text=f"{class_name}\n{start_time}-{end_time}",
                                   bg="lightblue", relief="raised")
            class_label.grid(row=self.time_to_row(start_hour, start_minute) + 1, column=day_column, rowspan=self.calculate_length(start_hour, start_minute, end_hour, end_minute), sticky="nsew", padx=2, pady=2)

        # Clear added inputs for the future
        self.class_name_entry.delete(0, tk.END)
        self.start_time_entry.delete(0, tk.END)
        self.end_time_entry.delete(0, tk.END)
        for day_var in self.day_vars:
            day_var.set("")

    def time_to_row(self, hour, minute):
        """Converts a 24-hour time (HH:MM) into the corresponding row index."""
        return (hour * 6) + (minute // 10)

    def calculate_length(self, start_hour, start_minute, end_hour, end_minute):
        """Calculates the length for a time block."""
        start_total_minutes = start_hour * 60 + start_minute
        end_total_minutes = end_hour * 60 + end_minute
        return (end_total_minutes - start_total_minutes) // 10

if __name__ == "__main__":
    BusynessManager()
