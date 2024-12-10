import customtkinter as ctk
from tkinter import filedialog

import fourier

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

    def create_interface(self):
        self.title("SVG Fourier Reconstruction")
        self.geometry("400x300")

        self.upload_button = ctk.CTkButton(self, text="Upload Image", command=self.upload_and_process_image)
        self.upload_button.pack(pady=20)

        self.coefficient_slider = ctk.CTkSlider(self, from_=1, to=100, orientation='horizontal', command=self.update_coefficient_label)
        self.coefficient_slider.set(50)
        self.coefficient_slider.pack(pady=20)

        self.coefficient_label = ctk.CTkLabel(self, text=f"Fourier Coefficients: {int(self.coefficient_slider.get())}")
        self.coefficient_label.pack()

        self.processing_label = ctk.CTkLabel(self, text="")
        self.processing_label.pack()

    def upload_and_process_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])

        if not file_path:
            self.processing_label.configure(text="")
            return

        self.processing_label.configure(text="Processing image...")  #
        self.update_idletasks()  # Update the GUI to show the label

        self.img = fourier.Fourier(file_path, self.coefficient_slider.get())
        self.img.process_paths()
        self.img.plot_fourier()

    def update_coefficient_label(self, value):
        self.coefficient_label.configure(text=f"Fourier Coefficients: {int(float(value))}")

    def capture_and_save_photo(self):
        self.processing_label.configure(text="Capturing photo...")

def main():
    app = App()
    app.create_interface()
    app.mainloop()

if __name__ == "__main__":
    main()




