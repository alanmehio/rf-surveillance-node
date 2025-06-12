from PySide6.QtCore import QObject, Signal


class GraphSignalManager(QObject):
    data_signal = Signal(list)

    def __init__(self)->None:
        super().__init__()

signal_manager = GraphSignalManager()