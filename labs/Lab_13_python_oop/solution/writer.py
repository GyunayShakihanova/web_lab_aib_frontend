import xlsxwriter
from base import BaseXlsBlock
from blocks import TopPayersBlock, TopCitiesBlock, AccountStatusBlock

class Writer:
    ANALYTICS_BLOCKS_CLASSES = [TopPayersBlock, TopCitiesBlock, AccountStatusBlock]

    def __init__(self, data):
        self.data = data

    def write_excel_report(self, output_file):
        with xlsxwriter.Workbook(output_file) as workbook:
            worksheet = workbook.add_worksheet()

            row = 0
            col = 0

            for block_class in self.ANALYTICS_BLOCKS_CLASSES:
                block_instance = block_class(worksheet, row, col, self.data)
                block_instance.write_header()
                block_instance.write_data()
                row += block_instance.get_row_increment()