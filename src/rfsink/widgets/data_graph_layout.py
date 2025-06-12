from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from rfsink.signal_manager.data_signal_manager import signal_manager
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np



class DataGraph3D(FigureCanvas):
    def __init__(self, figure:Figure=None)->None:        
        self.figure = Figure()
        super().__init__(figure)

        self.data = []
        self.freq = []
        self.pow = []
        self.time = []


        self.ax = self.figure.add_subplot(projection='3d')

        self.ax.set_title("Data Graph")
        
        signal_manager.data_signal.connect(self.receive_data)

        
                    
    def receive_data(self, data):
        self.data = data
        self.freq.clear()
        self.pow.clear()
        self.time.clear()

        for row_data in self.data:
            self.freq.append(row_data[1])
            self.pow.append(row_data[2])
            dt = datetime.strptime(row_data[3], "%d-%m-%Y %H:%M:%S")
            self.time.append(mdates.date2num(dt))

        self.draw_graph()

    
    def draw_graph(self):

        if not (self.freq and self.pow and self.time):
            print("No data to plot.")
            return
        self.ax.clear()

        self.ax.set_title("Data Graph")
        self.ax.set_xlabel("Frequency")
        self.ax.set_ylabel("Time")
        self.ax.set_zlabel("Power")
        print("Y-axis limits:", self.ax.get_ylim())
        self.ax.yaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
        self.ax.scatter(self.freq, self.time, self.pow)

        self.draw()

