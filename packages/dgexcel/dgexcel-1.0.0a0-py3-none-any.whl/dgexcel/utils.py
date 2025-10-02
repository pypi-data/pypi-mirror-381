from typing import Union, Optional, List, Dict
import os

from .excel_x import ExcelX
from .excel import Excel


def create_excel(list_: List[Union[Dict, List]], fname: str, header: Optional[List] = None,
                 column_width: Optional[List] = None, worksheet: str = 'Sheet', start_row: int = 0, borders=False):
    """
    Создает Excel-файл в формате xlsx или xls
    """
    fd, fn = os.path.split(fname)
    if fd:
        if not os.path.exists(fd):
            os.makedirs(fd)

    file_ext = fname.split('.')[-1].lower() if '.' in fname else 'xlsx'

    if file_ext == 'xlsx':
        create_xlsx(fname, list_, column_width, header, worksheet, start_row, borders)
    elif file_ext == 'xls':
        create_xls(fname, list_, column_width, header, worksheet, start_row, borders)
    else:
        # По умолчанию создаем xlsx
        create_xlsx(fname + '.xlsx', list_, column_width, header, worksheet, start_row, borders)


def create_xlsx(filename: str, data: List[Union[Dict, List]], column_width: Optional[List], header: Optional[List],
                sheet_name: str = 'Sheet', start_row: int = 1, add_borders: bool = False):
    """Создает xlsx файл используя ExcelX"""
    excel = ExcelX()
    excel.create_simple_excel(
        filename=filename,
        data=data,
        column_width=column_width,
        column_names=header,
        worksheet=sheet_name,
        rewrite=True,
        start_row=start_row + 1  # +1 потому что в ExcelX start_row=1 это первая строка
    )


def create_xls(filename: str, data: List[Union[Dict, List]], column_width: Optional[List], header: Optional[List],
               sheet_name: str = 'Sheet', start_row: int = 1, add_borders: bool = False):
    """Создает xls файл используя Excel"""
    excel = Excel()
    excel.create_simple_excel(
        filename=filename,
        data=data,
        column_width=column_width,
        column_names=header,
        worksheet=sheet_name,
        rewrite=True,
        start_row=start_row + 1  # +1 потому что в Excel start_row=1 это первая строка
    )


def read_excel(filename: str, excel_header: Union[list, dict], sheet_name: str = None,
               int_columns: list = None, date_columns: list = None, start_row: int = 1):
    """Читает Excel файл (поддерживает .xlsx и .xls)"""

    if filename.endswith('.xlsx'):
        # Используем ExcelX для чтения xlsx
        excel = ExcelX()
        excel.open_file(filename, rewrite=False)
        return excel.read_file(excel_header, sheet_name, int_columns, date_columns, start_row)

    else:
        # Используем Excel для чтения xls
        excel = Excel()
        excel.open_file(filename, rewrite=False)
        return excel.read_file(excel_header, sheet_name, int_columns, date_columns, start_row)