from PySide6 import QtWidgets
from rfsink.widgets.search_layout import SearchGroupBox
from rfsink.widgets.data_graph_layout import DataGraph3D
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLayout

class MainWindow(QtWidgets.QWidget):
   def __init__(self):
        super().__init__()


        self.layout = QtWidgets.QVBoxLayout(self)

        self.search = SearchGroupBox("Select minimun and maximum values")
        self.search.setMaximumHeight(200)
        self.layout.addWidget(self.search)

        self.graph = DataGraph3D()
        self.layout.addWidget(self.graph)
      


