from PySide6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

class TableResultsWindow(QMainWindow):
    def __init__(self, query):
        super().__init__()
        self.setWindowTitle("Query Results")
        
        # Create table view
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(len(query))
        self.table.setHorizontalHeaderLabels(["ID", "frequency", "power", "datetime"])


        for row, row_data in enumerate(query):
            for col, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(row, col, item)



        # Configure table
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.resizeColumnsToContents()
        
        self.setCentralWidget(self.table)
        self.resize(800, 600)

# Usage:
def show_query_results(query):
    global result_window
    result_window = TableResultsWindow(query)
    result_window.show()

