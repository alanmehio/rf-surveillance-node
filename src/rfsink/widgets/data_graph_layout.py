from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from rfsink.signal_manager.data_signal_manager import signal_manager, graph_type_manager
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
from scipy.interpolate import griddata



class DataGraph3D(FigureCanvas):
    def __init__(self, figure:Figure=None)->None:        
        self.figure = Figure()
        super().__init__(figure)

        self.min_power = 20.0
        self.max_power = 50.55

        self.type = "scatter"

        self.data = []
        self.freq = []
        self.pow = []
        self.time = []


        self.ax = self.figure.add_subplot(projection='3d')

        self.ax.set_title("Data Graph")
        
        signal_manager.data_signal.connect(self.receive_data)
        graph_type_manager.data_signal.connect(self.set_type)

        
                    
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

    def set_type(self, type):
        self.type = type
        self.draw_graph()

    
    def draw_graph(self):

        if not (self.freq and self.pow and self.time):
            print("No data to plot.")
            return
        self.ax.clear()
        
        if self.type == "scatter":

            self.ax.set_title("Data Graph")
            self.ax.set_xlabel("Frequency")
            self.ax.set_ylabel("Time")
            self.ax.set_zlabel("Power")
            self.ax.yaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
            self.ax.scatter(self.freq, self.time, self.pow)
            self.draw()

        elif self.type == "meshgrid":
            self.ax.clear()

            # Prepare data as numpy arrays
            freq = np.array(self.freq)
            time = np.array(self.time)
            power = np.array(self.pow)

            # Build a grid
            freq_lin = np.linspace(freq.min(), freq.max(), 30)
            time_lin = np.linspace(time.min(), time.max(), 30)
            FREQ, TIME = np.meshgrid(freq_lin, time_lin)

            # Interpolate power data onto grid
            POWER = griddata(
                points=(freq, time),
                values=power,
                xi=(FREQ, TIME),
                method='linear'
            )

            # Mask NaNs for better plotting
            POWER = np.nan_to_num(POWER, nan=np.nanmin(power))


            surf = self.ax.plot_surface(
                FREQ, TIME, POWER,
                cmap='inferno',
                linewidth=0.5,
                antialiased=True
            )
            
            self.ax.set_title("Data Graph")
            self.ax.set_xlabel("Frequency")
            self.ax.set_ylabel("Time")
            self.ax.set_zlabel("Power")

            self.ax.set_ylim(time.min(), time.max())
            self.ax.yaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
            self.ax.yaxis.set_major_locator(mdates.AutoDateLocator())

            self.ax.set_zlim(self.min_power, self.max_power)

            self.draw()

