from pathlib import Path
from typing import *
import json
import os

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

BASE_DIR = Path(__file__).resolve().parent
PATH_TO_CURRENT_TAGS = BASE_DIR / 'current_tags.json'


class Logic:
    def __init__(self, data_path: Path = PATH_TO_CURRENT_TAGS):
        self.path_to_current_tags = Path(data_path)

    def __load_tags(self) -> dict:
        with open(self.path_to_current_tags, 'r', encoding='utf-8') as file:
            data = dict(json.load(file))
        return data['tags']

    def get_tags(self) -> dict:
        return self.__load_tags()

    def get_tag_color_names(self) -> List[str]:
        return list(self.get_tags().keys())

    def normalize_color(self, color_name: str) -> str:
        return {'red': '#ff5858', 'green': '#88ff88', 'blue': '#6096ff', 'yellow': '#fff497', 'pink': '#ff7ce7', 'purple': '#ba5dff', 'orange': '#ffc36f', 'tan': '#d6c7a7', }.get(color_name, color_name)

    def get_tag_colors(self) -> List[str]:
        return [self.normalize_color(color_name) for color_name in self.get_tag_color_names()]

    def get_tag_names(self) -> List[str]:
        return [tag_data['name'] for tag_data in self.get_tags().items()]

    def get_tag_paths(self, tag_key: Optional[str] = None) -> List[str]:
        tags = self.get_tags()
        if not tags:
            return []

        if tag_key is None:
            tag_key = next(iter(tags))

        tag_content = dict(tags[tag_key])
        return [value for key, value in tag_content.items() if str(key).startswith('path') and value]

    def get_first_tag(self) -> dict:
        return next(iter(self.get_tags().values()), {})

    def add_path_to_files_tree_model(self, icon_provider: QFileIconProvider, path: str, parent_item: QStandardItem):
        if not os.path.exists(path):
            return

        file_info = QFileInfo(path)
        name_item = QStandardItem(file_info.fileName())
        name_item.setIcon(icon_provider)

        path_item = QStandardItem(path)
        parent_item.appendRow([name_item, path_item])
