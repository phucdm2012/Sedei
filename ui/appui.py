from PySide6.QtWidgets import *
from .file_tree_widget import FileTreeWidget
from tag.tag import TagWidget

class AppUI(QWidget):
    def __init__(self):
        super().__init__()
        
