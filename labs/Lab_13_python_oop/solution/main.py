from datetime import datetime
import json
import os
from writer import Writer

def load_data(file_path):
    full_path = os.path.join(os.getcwd(), file_path)
    with open(full_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def generate_report_filename():
    timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return os.path.join(os.getcwd(), f'my_payments_analytics_{timestamp}.xlsx')

def main():
    clients_data = load_data('clients.json')['clients']
    payments_data = load_data('payments.json')['payments']

    data = {'clients': clients_data, 'payments': payments_data}
    output_file = generate_report_filename()

    xls_writer = Writer(data)
    xls_writer.write_excel_report(output_file)

    print(f"Report generated successfully. Output file: {output_file}")

if __name__ == '__main__':
    main()