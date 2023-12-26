from base import BaseXlsBlock
from datetime import datetime
from collections import defaultdict

class TopBlock(BaseXlsBlock):
    def write_header(self):
        self.worksheet.write(self.row, self.col, f"**{self.NAME}**")

class TopPayersBlock(TopBlock):
    NAME = "Отчёт по активным клиентам"

    def write_data(self):
        self.row += 1
        clients, payments = self.data['clients'], self.data['payments']

        quarterly_payments = defaultdict(lambda: defaultdict(float))
        for payment in payments:
            client_id, amount = payment['client_id'], payment['amount']
            created_at = datetime.strptime(payment['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            quarter = (created_at.month - 1) // 3 + 1
            quarterly_payments[client_id][quarter] += amount

        top_payers = [{'client_id': cid, 'total_amount': sum(data.values())} for cid, data in quarterly_payments.items()]
        top_payers.sort(key=lambda x: x['total_amount'], reverse=True)
        top_payers = top_payers[:10]

        for i, payer in enumerate(top_payers, start=1):
            client_info = next(client for client in clients if client['id'] == payer['client_id'])
            self.worksheet.write(self.row + i, self.col, f"{i}. **{client_info['fio']}**: {payer['total_amount']}")

class TopCitiesBlock(TopBlock):
    NAME = "География клиентов"

    def write_data(self):
        self.row += 1
        clients = self.data['clients']

        city_counts = defaultdict(int)
        for client in clients:
            city_counts[client['city']] += 1

        top_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (city, count) in enumerate(top_cities, start=1):
            self.worksheet.write(self.row + i, self.col, f"{i}. **{city}**: {count} клиентов")

class AccountStatusBlock(TopBlock):
    NAME = "Анализ состояния счёта"

    def write_data(self):
        self.row += 1
        clients, payments = self.data['clients'], self.data['payments']

        account_balances = defaultdict(float)
        for payment in payments:
            client_id, amount = payment['client_id'], payment['amount']
            account_balances[client_id] += amount

        top_balances = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (client_id, balance) in enumerate(top_balances, start=1):
            client_info = next(client for client in clients if client['id'] == client_id)
            self.worksheet.write(self.row + i, self.col, f"{i}. **{client_info['fio']}**: Баланс - {balance}")