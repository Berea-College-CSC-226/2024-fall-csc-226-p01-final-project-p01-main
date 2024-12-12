import cv2
import svgwrite
import fourier

class PhotoCapture:
    def __init__(self, processing_label, coefficient_slider):
        self.processing_label = processing_label
        self.coefficient_slider = coefficient_slider

    def capture_and_save_photo(self):
        self.processing_label.configure(text="Processing image...")
        self.processing_label.update_idletasks()

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.processing_label.configure(text="")
            return

        ret, frame = cap.read()
        if not ret:
            cap.release()
            self.processing_label.configure(text="")
            return

        frame = cv2.rotate(frame, cv2.ROTATE_180)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        dwg = svgwrite.Drawing('cam.svg', profile='tiny')

        for contour in contours:
            points = []
            for point in contour:
                x = float(point[0][0])
                y = float(point[0][1])
                points.append((x, y))
            dwg.add(dwg.polyline(points, stroke='black', fill='none'))

        dwg.save()

        cap.release()

        self.process_svg_file('cam.svg')

        self.processing_label.configure(text="")

    def process_svg_file(self, file_path):
        img = fourier.Fourier(file_path, self.coefficient_slider.get())
        img.process_paths()
        img.plot_fourier()
