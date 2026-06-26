from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys


class FileTreeWidget(QTreeView):
    def __init__(self):
        super().__init__()
        self.setAnimated(True)

        self.files_model = QFileSystemModel()
        self.files_model.setRootPath('')

        self.setModel(self.files_model)
        self.setRootIndex(QModelIndex())
        self.hide_other_column()

    def hide_other_column(self):
        for i in range(1, 4):
            self.hideColumn(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileTreeWidget()
    window.show()
    sys.exit(app.exec())
