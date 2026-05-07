
# Imports
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from core.keys_manager import keys_detector_manager

# GUI Class
class gui:

    # Constructor
    def __init__(self):
        self.keys_detector = None
        self.logic = None
        self.keys_detector = None
        self.root = None
        self.frecuencias = []
        self.max_points = 50

    # Create GUI
    def create_gui(self):

        # Create main window
        self.root = tk.Tk()
        self.root.title("Monitor Cardiaco")
        self.root.geometry("800x600")

        # Create keys detector
        self.keys_detector = keys_detector_manager()
        self.keys_detector.start()
        self.logic = self.keys_detector.logic

        # Create elements
        self.__create_widgets()
        self.__update_ui()
        self.root.mainloop()
    
    # UI elements
    def __create_widgets(self):

        # Graphic
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [])
        self.ax.set_title("Frecuencia Cardiaca")
        self.ax.set_ylim(60, 120)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        # Gyroscope
        self.label_gyro = tk.Label(self.root, text="X: 0   Y: 0   Z: 0", font=("Arial", 14))
        self.label_gyro.pack(pady=10)

        # Cardiac frecuency
        self.label_frecuency = tk.Label(self.root, text="Frecuencia: 0", font=("Arial", 14))
        self.label_frecuency.pack()

        # Button group
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=20)

        # Frecuency button
        btn1 = ttk.Button(frame_buttons, text="Subir Frecuencia", command=self.logic.increase_frecuency)
        btn1.grid(row=0, column=0, padx=10)

        # Gyroscope button
        btn2 = ttk.Button(frame_buttons, text="Generar Movimiento", command=self.logic.increase_gyroscope)
        btn2.grid(row=0, column=1, padx=10)

        # Increase both button
        btn3 = ttk.Button(frame_buttons, text="Subir Ambos", command=self.logic.increase_both)
        btn3.grid(row=0, column=2, padx=10)

        # Toggle alarm button
        btn4 = ttk.Button(frame_buttons, text="Activar Alarma", command=self.logic.toggle_alarm)
        btn4.grid(row=0, column=3, padx=10)

    # Update UI
    def __update_ui(self):

        # Get value of cardiac frecuency
        freq = int(self.logic.get_frecuency())
        self.frecuencias.append(freq)

        if len(self.frecuencias) > self.max_points:
            self.frecuencias.pop(0)

        self.label_frecuency.config(text=f"Frecuencia: {freq}")

        # Draw line in canvas
        self.line.set_data(range(len(self.frecuencias)), self.frecuencias)
        self.ax.set_xlim(0, self.max_points)
        self.canvas.draw()

        # Get values of Gyroscope
        x = self.logic.get_x()
        y = self.logic.get_y()
        z = self.logic.get_z()
        self.label_gyro.config(text=f"X: {x}   Y: {y}   Z: {z}")

        # Activate alarm if values are critic
        self.logic.verification_flags(max_frecuency=100, x=5, y=8, z=9)

        # Loop each 500ms
        self.root.after(500, self.__update_ui)

#  \____/\
#  /\``/\
# -byRyanAg...