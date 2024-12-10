import unittest
from gdp_calculator import GDPComponent, GDPCalculator


class TestGDPComponents(unittest.TestCase):
    def test_gdp_component_value(self):
        # Test if GDPComponent can store and retrieve values
        component = GDPComponent("Test")
        component.set_value(200)
        self.assertEqual(component.get_value(), 200, "Component value mismatch.")

    def test_gdp_calculator(self):
        # Test if GDPCalculator correctly sums components
        c1 = GDPComponent("Consumption")
        c1.set_value(100)
        c2 = GDPComponent("Investment")
        c2.set_value(200)

        calculator = GDPCalculator()
        calculator.add_component(c1)
        calculator.add_component(c2)

        self.assertEqual(calculator.calculate_gdp(), 300, "GDP calculation mismatch.")


if __name__ == "__main__":
    unittest.main()

import unittest
import tkinter as tk
from gdp_calculator import GDPApp


class TestGDPApp(unittest.TestCase):
    def test_calculate_gdp(self):
        # Create a Tkinter root window
        root = tk.Tk()
        app = GDPApp(root)

        # Simulate user input
        app.consumption_entry.insert(0, "100")
        app.investment_entry.insert(0, "200")
        app.government_entry.insert(0, "300")
        app.net_exports_entry.insert(0, "50")

        # Simulate button click
        app.calculate_button.invoke()

        # Check the result
        self.assertEqual(app.result_label.cget("text"), "Overall GDP:$ 650.00")

        root.destroy()


if __name__ == "__main__":
    unittest.main()
