import xlsxwriter
from blocks import HeaderBlock, PayersBlock, CitiesBlock, BankAccountBlock

class Writer:
    CLASSES = [
        HeaderBlock,
        PayersBlock,
        CitiesBlock,
        BankAccountBlock
    ]

    def __init__(self, data):
        self.data = data

    def write_excel(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:Z', 35)
        row = 0
        col = 0

        for i in range(0, len(self.CLASSES)):
            worksheet.set_column(i,i,30)
            block_instance = self.CLASSES[i](worksheet, workbook, row, col, self.data)
            block_instance.write_header()
            block_instance.write_data()

        workbook.close()