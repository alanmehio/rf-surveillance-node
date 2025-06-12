from PySide6.QtCore import QObject, Signal


class GraphSignalManager(QObject):
    data_signal = Signal(list)

    def __init__(self)->None:
        super().__init__()

signal_manager = GraphSignalManager()

class GraphTypeSignalManager(QObject):
    data_signal = Signal(str)

    def __init__(self)->None:
        super().__init__()

graph_type_manager = GraphTypeSignalManager()