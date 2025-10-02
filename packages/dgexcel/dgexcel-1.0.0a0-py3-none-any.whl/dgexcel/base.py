from typing import Union, Optional, List, Dict, Iterable
from datetime import datetime, date
import os


class ExcelBase:
    def __init__(self, filename: str = None):
        self.filename = filename
        self.styles = {}
        self.workbook = None
        self.worksheets = {}
        self.current_worksheet = None
        self.rows_qty: int = 0

    def get_file(self):
        raise NotImplementedError(f'Method get_file not implemented in class {self.__class__.__name__}')

    def create_file(self):
        raise NotImplementedError(f'Method create_file not implemented in class {self.__class__.__name__}')

    def open_file(self, filename: str = None):
        if filename:
            self.filename = filename
        try:
            fd, fn = os.path.split(self.filename)
            if fd:
                self._check_folder_exist(fd)
        except TypeError:
            pass

    def save_file(self):
        raise NotImplementedError(f'Method save_name not implemented in class {self.__class__.__name__}')

    def add_worksheet(self, worksheet: str):
        raise NotImplementedError(f'Method add_worksheet not implemented in class {self.__class__.__name__}')

    def rename_worksheet(self, worksheet_old: str, worksheet_new: str):
        raise NotImplementedError(f'Method rename_worksheet not implemented in class {self.__class__.__name__}')

    def select_worksheet(self, worksheet):
        self.current_worksheet = self.worksheets.get(worksheet)

    def add_cell(self, row: int, col: int, value: Union[None, str, float, int, date, datetime],
                 style: Optional[Dict] = None):
        raise NotImplementedError(f'Method add_cell not implemented in class {self.__class__.__name__}')

    def add_cell_coords(self, coords: str, value: Union[None, str, float, int, date, datetime],
                        style: Optional[Dict] = None):
        raise NotImplementedError(f'Method add_cell_coords not implemented in class {self.__class__.__name__}')

    def add_row(self, row: int, list_cells: Iterable[Union[None, str, float, int, date, datetime]],
                start_col: int = 0, styles: Union[None, List, Dict] = None):
        raise NotImplementedError(f'Method add_row not implemented in class {self.__class__.__name__}')

    def add_column(self, col: int, list_cells: Iterable[Union[None, str, float, int, date, datetime]],
                   start_row: int = 1, styles: Union[None, List, Dict] = None):
        raise NotImplementedError(f'Method add_column not implemented in class {self.__class__.__name__}')

    def add_merge_cell(self, first_row: int, first_col: int, last_row: int, last_col: int,
                       value: Union[None, str, float, int, date, datetime], style: Optional[Dict] = None):
        raise NotImplementedError(f'Method add_merge_row not implemented in class {self.__class__.__name__}')

    def add_merge_cell_coords(self, first_coords: str, last_coords,
                              value: Union[None, str, float, int, date, datetime], style: Optional[Dict] = None):
        raise NotImplementedError(f'Method add_merge_cell_coords not implemented in class {self.__class__.__name__}')

    def add_list_rows(self, first_row: int, first_col, list_rows: List, styles: Union[None, List, Dict] = None):
        raise NotImplementedError(f'Method add_list_rows not implemented in class {self.__class__.__name__}')

    def set_cell_dimension(self, row: int, col: int, height: int = 15, width: int = 10):
        raise NotImplementedError(f'Method set_cell_dimension not implemented in class {self.__class__.__name__}')

    def set_columns_width(self, list_columns_width: List[int], start_col: int = 1):
        raise NotImplementedError(f'Method set_columns_width not implemented in class {self.__class__.__name__}')

    def set_rows_height(self, list_rows_height: List[int], start_row: int = 1):
        raise NotImplementedError(f'Method set_rows_height not implemented in class {self.__class__.__name__}')

    def create_simple_excel(self, filename, data: List[Union[Dict, List]], column_width: Optional[List] = None,
                            column_names: Optional[List] = None, styles: Union[None, List, Dict] = None):
        raise NotImplementedError(f'Method create_simple_excel not implemented in class {self.__class__.__name__}')

    def get_max_row(self):
        raise NotImplementedError(f'Method get_max_row not implemented in class {self.__class__.__name__}')

    def get_max_column(self):
        raise NotImplementedError(f'Method get_max_column not implemented in class {self.__class__.__name__}')

    def read_file(self, excel_header: Union[list, dict], sheet_name: str = None,
                  int_columns: list = None, date_columns: list = None, start_row: int = 1):
        raise NotImplementedError(f'Method read_file not implemented in class {self.__class__.__name__}')

    def _check_folder_exist(self, folder: str):
        """Проверяет существование папки и создает ее при необходимости"""
        if not os.path.exists(folder):
            os.makedirs(folder)

    def _parse_date(self, date_str: str) -> datetime:
        """Парсит дату из строки в различных форматах"""
        from datetime import datetime
        formats = [
            '%d.%m.%Y', '%d.%m.%y', '%d/%m/%Y', '%d/%m/%y',
            '%Y-%m-%d', '%d-%m-%Y', '%d-%m-%y'
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Не удалось распарсить дату: {date_str}")