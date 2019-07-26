from openpyxl import Workbook

class Excel(object) :
    def create_workbook(self, data):
        wb  = Workbook
        ws1 = wb.active
        for value in data['matches']:
            print(value)

