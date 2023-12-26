from abc import ABC, abstractmethod

class BaseXlsBlock(ABC):
    ROW_INCREMENT = 12

    def __init__(self, worksheet, row, col, data):
        self.worksheet, self.row, self.col, self.data = worksheet, row, col, data

    @abstractmethod
    def write_header(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

    def get_row_increment(self):
        return self.ROW_INCREMENT