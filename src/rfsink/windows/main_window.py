from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from rfsink.widgets.search_layout import SearchGroupBox
from rfsink.widgets.data_graph_layout import DataGraph3D
from PySide6.QtGui import QAction, QActionGroup
from rfsink.signal_manager.data_signal_manager import graph_type_manager

class MainWindow(QMainWindow):
   def __init__(self):
        super().__init__()


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.search = SearchGroupBox("Select minimum and maximum values")
        self.search.setMaximumHeight(200)
        layout.addWidget(self.search)

        self.graph = DataGraph3D()
        layout.addWidget(self.graph)

        self.setWindowTitle("RF Sink Viewer")
        self.resize(800, 600)

        # Create the menu bar
        self.create_menu()



   def create_menu(self):
       menubar = self.menuBar()
   
       file_menu = menubar.addMenu("File")
   
       exit_action = QAction("Exit", self)
       exit_action.triggered.connect(self.close)
       file_menu.addAction(exit_action)
   
       help_menu = menubar.addMenu("Help")
   
       about_action = QAction("About", self)
       about_action.triggered.connect(self._show_about)
       help_menu.addAction(about_action)


       # parrent menu
       tool_menu = menubar.addMenu("Tools")
       select_tool_menu = tool_menu.addMenu("3D Graph")

       graph_group = QActionGroup(self)
       graph_group.setExclusive(True)

       graph_option_a = QAction("3D Scatter Plot", self, checkable=True)
       graph_option_a.setChecked(True)
       graph_option_a.triggered.connect(self.set_scatter)
       
       graph_option_b = QAction("3D Mesh Grid", self, checkable=True)
       graph_option_b.triggered.connect(self.set_meshgrid)

       graph_group.addAction(graph_option_a)
       graph_group.addAction(graph_option_b)

       select_tool_menu.addAction(graph_option_a)
       select_tool_menu.addAction(graph_option_b)


   def _show_about(self):
      QtWidgets.QMessageBox.about(self, "About", "RF Sink Viewer using PySide6")

   def set_scatter(self):
      graph_type_manager.data_signal.emit("scatter")
      
   def set_meshgrid(self):
      graph_type_manager.data_signal.emit("meshgrid")