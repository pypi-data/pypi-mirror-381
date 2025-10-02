"""
DGExcel - Пакет для работы с Excel файлами
"""

from .excel_x import ExcelX
from .excel import Excel
from .constants import BORDER, FONT, NUMBER_FORMAT
from .utils import create_excel, read_excel

# Для обратной совместимости
try:
    from .utils import create_xls, create_xlsx
except ImportError:
    pass

__version__ = "1.0.0"
__all__ = ['ExcelX', 'Excel', 'BORDER', 'FONT', 'NUMBER_FORMAT',
           'create_excel', 'read_excel']