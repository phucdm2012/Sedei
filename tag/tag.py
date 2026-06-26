from PySide6.QtWidgets import QWidget, QHBoxLayout, QTreeView, QFileIconProvider
from PySide6.QtGui import QStandardItemModel
from .logic import Logic


class TagPaneWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tag_widget_main_layout = QHBoxLayout()
        self.setLayout(self.tag_widget_main_layout)

        self.logic = Logic()
        self.tag_content = self.logic.get_tag_paths()

        self.files_model = QStandardItemModel()
        self.files_model.setHorizontalHeaderLabels(['Name', 'Path'])

        self.icon_provider = QFileIconProvider()

        for path in self.tag_content:
            self.logic.add_path_to_files_tree_model(self.icon_provider, path, self.files_model.invisibleRootItem())

        self.create_tree_view()

    def create_tree_view(self):
        self.tag_tree_view = QTreeView()
        self.tag_tree_view.setModel(self.files_model)
        self.tag_tree_view.setColumnWidth(0, 200)
        self.tag_widget_main_layout.addWidget(self.tag_tree_view)
