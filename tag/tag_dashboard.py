from PySide6.QtWidgets import *
from .logic import Logic


class TagDashBoard(QDialog):
    def __init__(self):
        super().__init__()
        self.logic = Logic()
        self.tag_names = self.logic.get_tag_names()
        self.tag_colors = self.logic.get_tag_colors()

        self.tag_dashboard_layout = QHBoxLayout()
        self.setLayout(self.tag_dashboard_layout)

        for tag_name, tag_color in zip(self.tag_names, self.tag_colors):
            self.create_tag_item(tag_name, tag_color)

    def create_tag_item(self, tag_name: str, tag_color: str):
        self.tag_dashboard_layout.addWidget(TagItem(tag_name, tag_color))


class TagItem(QWidget):
    def __init__(self, tag_name: str, tag_color: str):
        super().__init__()
        self.__set_bg_color(tag_color)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setOffset(2, 4)

        self.setGraphicsEffect(self.shadow)

        self.tag_item_layout = QHBoxLayout()
        self.tag_item_name_label = QLabel(tag_name)
        self.tag_item_layout.addWidget(self.tag_item_name_label)
        self.setLayout(self.tag_item_layout)

    def __set_bg_color(self, color: str):
        self.setStyleSheet(f'background-color: {color}')
