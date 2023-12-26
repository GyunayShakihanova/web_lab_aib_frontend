from abc import ABCMeta, abstractmethod


class BaseBlock(metaclass=ABCMeta):
    def __init__(self, worksheet, workbook, row, col, data):
        self.worksheet = worksheet
        self.workbook = workbook
        self.row = row
        self.col = col
        self.data = data
        self.header_format = {
            'border': 2,
            'color': '#002060',
            'bold': True,
            'bg_color': '#FCD5B4',
            'font_size': 14,
            'font_name': 'Arial'
        }

        self.title_format = {
            'bold': True,
            'bg_color': '#C5D9F1',
            'border': 3,
            'font_size': 10,
            'font_name': 'Arial'
        }

        self.title2_format = {
            'bold': False,
            'bg_color': '#C5D9F1',
            'border': 3,
            'font_size': 10,
            'font_name': 'Arial'
        }

    @abstractmethod
    def write_header(self):
        pass

    @abstractmethod
    def write_data(self):
        pass