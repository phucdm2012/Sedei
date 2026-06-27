from PySide6.QtWidgets import *
from .appui import AppUI


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.app_main_layout = QHBoxLayout()
        self.app_ui_layout = QVBoxLayout()

        app_ui = AppUI()
        self.app_ui_layout.addWidget(app_ui)

        self.app_main_layout.addLayout(self.app_ui_layout)
        self.setLayout(self.app_main_layout)

        self.custom_mainwindow_view()

    def custom_mainwindow_view(self):
        self.app_main_layout.setContentsMargins(0, 0, 0, 0)
        self.app_ui_layout.setContentsMargins(0, 0, 0, 0)

        self.resize(1200, 800)
