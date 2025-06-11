from PySide6 import QtWidgets
from rfsink.widgets.search_layout import SearchGroupBox
from PySide6.QtCore import Qt

class MainWindow(QtWidgets.QWidget):
   def __init__(self):
        super().__init__()


        self.layout = QtWidgets.QVBoxLayout(self)

        self.search = SearchGroupBox("Select minimun and maximum values")
        self.search.setMaximumHeight(200)
        self.search.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.search, alignment=Qt.AlignmentFlag.AlignTop)
      


