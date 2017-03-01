import openpyxl
import mmap
from openpyxl.worksheet import Worksheet


class Excel(object):
    file_name = None
    sheets = []
    wb = None

    def __init__(self, file_name):
        if not file_name:
            raise Exception("File not found "+file_name)
        self.file_name = file_name
        self.wb = openpyxl.load_workbook(file_name)
        sheet_names = self.wb.get_sheet_names()
        for sheet_name in sheet_names:
            sheet_obj = self.wb.get_sheet_by_name(sheet_name)
            if sheet_obj:
                sheet = Sheet(self.wb, sheet_obj, sheet_name)
                self.sheets.append(sheet)


    def get_data_for_range_from_sheet(self, start, end, sheet_name):
        sheet = self.wb.get_sheet_by_name(sheet_name)
        data = {}
        for rowCells in sheet[start:end]:
            for cell in rowCells:
                data[cell.coordinate] = cell.value

        return data
        



class Sheet(object):
    title = None
    wb = None
    sheet = None
    is_active = False


    def __init__(self, wb, sheet, title):
        self.wb = wb
        self.sheet = sheet
        self.title = title

    def _read_cells(self):
        print ''



class Cell(object):
    coordinate = None
    value = None

    def __init__(self, coordinate, value):
        self.coordinate = coordinate
        self.value = value

    def get(self):
        return (self.coordinate, self.value)
