from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .file_tree_widget import FileTreeWidget
from tag.tag import TagPanelWidget

class AppUI(QSplitter):
    def __init__(self, orientation=Qt.Orientation.Horizontal):
        super().__init__()

        self.file_tree_widget = FileTreeWidget()
        self.tag_panel_widget = TagPanelWidget()

        self.addWidget(self.file_tree_widget)
        self.addWidget(self.tag_panel_widget)

        self.setSizes([400, 800])
