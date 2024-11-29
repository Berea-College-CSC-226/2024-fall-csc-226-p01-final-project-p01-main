
#Name: Feda Mohammadi
#Username: mohammadif
########################################################################################################################
#Purpose: This program calculates the GDP using user-provided inputs for its components.

########################################################################################################################
#Acknowledgment: resources and mentors for guidance on GDP and GUI programming.

########################################################################################################################

import tkinter as tk
from tkinter import messagebox  # For error handling messages

# Class for individual GDP components
class GDPComponent:
    def __init__(self, name):
        self.component_name = name
        self.value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Class for calculating total GDP
class GDPCalculator:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def calculate_gdp(self):
        total_gdp = sum(component.get_value() for component in self.components)
        return total_gdp


# GUI application class
class GDPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GDP Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.config(bg="#f7f7f7")  # Background color

        # GDP components
        self.consumption = GDPComponent("Consumption")
        self.investment = GDPComponent("Investment")
        self.government_spending = GDPComponent("Government Spending")
        self.net_exports = GDPComponent("Net Exports")

        self.gdp_calculator = GDPCalculator()
        self.gdp_calculator.add_component(self.consumption)
        self.gdp_calculator.add_component(self.investment)
        self.gdp_calculator.add_component(self.government_spending)
        self.gdp_calculator.add_component(self.net_exports)

        # Title label
        self.title_label = tk.Label(root, text="GDP Calculator", font=("Helvetica", 18, "bold"), bg="#f7f7f7")
        self.title_label.pack(pady=10)

        # Welcome message displayed on the same page
        self.create_welcome_message()

        # Input fields
        self.consumption_entry = self.create_input_field("Consumption (C): $")
        self.investment_entry = self.create_input_field("Investment (I): $")
        self.government_entry = self.create_input_field("Government Spending (G): $")
        self.net_exports_entry = self.create_input_field("Net Exports (NX): $")

        # Buttons
        self.calculate_button = tk.Button(root, text="Calculate GDP", command=self.calculate_gdp, bg="#4CAF50", fg="white", width=20)
        self.calculate_button.pack(pady=15)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_inputs, bg="#f44336", fg="white", width=20)
        self.reset_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(root, text="Overall GDP:$ ", font=("Helvetica", 12, "bold"), bg="#f7f7f7")
        self.result_label.pack(pady=10)

    def create_welcome_message(self):
        """
        Display a welcome message with brief information about GDP and its components.
        """
        message = (
            "Welcome to the GDP Calculator!\n\n"
            "What is GDP?\nGross Domestic Product (GDP) measures the total economic output of a country \n within a year.\n\n"
            "Components of GDP:\n"
            "Consumption (C): Total spending by households.\n"
            "Investment (I): Expenditure on goods used for future production.\n"
            "Government Spending (G): Expenditure by the government on goods and services.\n"
            "Net Exports (NX): Exports minus imports."
        )

        self.welcome_frame = tk.LabelFrame(self.root, text="Welcome", font=("Helvetica", 10, "bold"), bg="#f7f7f7", width=450)
        self.welcome_frame.pack(pady=10)

        self.welcome_label = tk.Label(self.welcome_frame, text=message, font=("Helvetica", 9), bg="#f7f7f7", justify="left", anchor="w")
        self.welcome_label.pack(padx=10, pady=10)

    def create_input_field(self, label_text):
        """
        Create a labeled input field with tooltip for GDP components.
        """
        label = tk.Label(self.root, text=label_text, font=("Helvetica", 10, "bold"), bg="#f7f7f7")
        label.pack()

        entry_var = tk.Entry(self.root, width=30)
        entry_var.pack(pady=5)

        # Tooltip for guidance
        tooltip = f"Enter the value for {label_text.split(':')[0]}"
        entry_var.bind("<Enter>", lambda e: self.show_tooltip(e, tooltip))
        entry_var.bind("<Leave>", self.hide_tooltip)

        return entry_var

    def show_tooltip(self, event, text):
        """
        Display a tooltip when hovering over input fields.
        """
        self.tooltip = tk.Label(self.root, text=text, bg="yellow", font=("Helvetica", 8))
        self.tooltip.place(x=event.widget.winfo_x() + event.widget.winfo_width() + 10, y=event.widget.winfo_y())

    def hide_tooltip(self, event):
        """
        Hide the tooltip.
        """
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()

    def calculate_gdp(self):
        """
        Retrieve user input, update component values, calculate GDP, and display it.
        """
        try:
            # Get user input and update components
            self.consumption.set_value(float(self.consumption_entry.get()))
            self.investment.set_value(float(self.investment_entry.get()))
            self.government_spending.set_value(float(self.government_entry.get()))
            self.net_exports.set_value(float(self.net_exports_entry.get()))

            # Calculate GDP
            total_gdp = self.gdp_calculator.calculate_gdp()

            # Display the result
            self.result_label.config(text=f"Overall GDP:$ {total_gdp:.2f}")
        except ValueError:
            # Handle the invalid inputs
            messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

    def reset_inputs(self):
        """
        Clear all input fields and reset the result label.
        """
        self.consumption_entry.delete(0, tk.END)
        self.investment_entry.delete(0, tk.END)
        self.government_entry.delete(0, tk.END)
        self.net_exports_entry.delete(0, tk.END)
        self.result_label.config(text="Overall GDP:$ ")


# This is the main code to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GDPApp(root)
    root.mainloop()
