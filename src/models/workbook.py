from openpyxl import Workbook
import os

class WorkbookGenerator:
    def __init__(self, header):
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.title = 'Report'
        self.create_header(header)

    def create_header(self, header):
        for col, val in enumerate(header, start = 1):
            self.worksheet.cell(row = 1, column = col, value = val)
            
        self.save_reports_in_folder()

    
    def save_reports_in_folder(self):
        reports = 'reports/'
        if not os.path.exists(reports):
            os.mkdir(reports)
        
        file_name = 'report.xlsx'
        path_folder = reports + file_name
        self.workbook.save(path_folder)
