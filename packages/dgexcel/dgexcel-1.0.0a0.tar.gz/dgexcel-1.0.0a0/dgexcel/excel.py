from string import printable
from typing import Union, Optional, List, Dict, Iterable
from datetime import datetime, timedelta, date
import os

from .base import ExcelBase
from .constants import BORDER, FONT, NUMBER_FORMAT


class Excel(ExcelBase):
    """
    Класс для работы со старыми форматами Excel (.xls)
    Требует установки пакета с опцией [xls]: pip install dgexcel[xls]
    """

    def __init__(self, filename: str = None):
        super().__init__(filename)
        self._check_xls_dependencies()

    def _check_xls_dependencies(self):
        """Проверяет наличие зависимостей для работы с xls"""
        try:
            import xlwt
            import xlrd
        except ImportError:
            raise ImportError(
                "Для работы с .xls файлами требуются xlwt и xlrd. "
                "Установите пакет с опцией [xls]: pip install dgexcel[xls]"
            )

    def open_file(self, filename: str = None, rewrite=True):
        if filename and not filename.endswith('xls'):
            filename += '.xls'

        super().open_file(filename=filename)

        if os.path.exists(self.filename) and not rewrite:
            self.get_file()
        else:
            self.create_file()

    def get_file(self):
        import xlrd
        self.workbook = xlrd.open_workbook(self.filename)
        # Создаем словарь листов
        self.worksheets = {sheet.name: sheet for sheet in self.workbook.sheets()}
        self.current_worksheet = self.workbook.sheet_by_index(0)

    def create_file(self):
        import xlwt
        self.workbook = xlwt.Workbook()
        # Создаем активный лист по умолчанию
        self.add_worksheet('Sheet1')

    def add_worksheet(self, worksheet: str):
        import xlwt
        if not hasattr(self, 'workbook') or self.workbook is None:
            self.create_file()
        self.worksheets[worksheet] = self.workbook.add_sheet(worksheet)
        if not self.current_worksheet:
            self.current_worksheet = self.worksheets[worksheet]

    def rename_worksheet(self, worksheet_old: str, worksheet_new: str):
        # В xlwt переименование листов не поддерживается напрямую
        # Создаем новый лист и копируем данные
        if worksheet_old in self.worksheets:
            # Сохраняем данные старого листа
            old_sheet = self.worksheets[worksheet_old]

            # Создаем новый лист
            self.add_worksheet(worksheet_new)

            # Копируем данные (упрощенная версия)
            # В реальной реализации нужно скопировать все ячейки и стили

            # Удаляем старый лист из словаря
            del self.worksheets[worksheet_old]

            self.select_worksheet(worksheet_new)

    def select_worksheet(self, worksheet):
        if not self.worksheets.get(worksheet):
            self.add_worksheet(worksheet)
        self.current_worksheet = self.worksheets.get(worksheet)

    def save_file(self, new_filename: str = None):
        filename = self.filename if not new_filename else new_filename
        if not filename.endswith('.xls'):
            filename += '.xls'
        self.workbook.save(filename)

    def _get_style(self, style: Optional[Dict] = None):
        """Создает xlwt стиль на основе словаря стилей"""
        import xlwt

        if not style:
            return xlwt.XFStyle()

        xlwt_style = xlwt.XFStyle()

        # Обработка шрифта
        font = xlwt.Font()
        if style.get('bold'):
            font.bold = True
        if style.get('italic'):
            font.italic = True
        if style.get('font'):
            f = style.get('font')
            font.name = f.get('name', 'Calibri')
            font.height = f.get('size', 11) * 20  # xlwt использует 1/20 точки
            font.bold = f.get('bold', False)
            font.italic = f.get('italic', False)
            font.underline = f.get('underline', False)
            font.struck_out = f.get('strike', False)
            font.colour_index = self._color_to_index(f.get('color', '000000'))

        xlwt_style.font = font

        # Обработка границ
        if style.get('border'):
            borders = xlwt.Borders()
            b = style.get('border')

            left = b.get('left', {})
            if left.get('style') == 'thin':
                borders.left = xlwt.Borders.THIN
            if left.get('color'):
                borders.left_colour = self._color_to_index(left.get('color'))

            right = b.get('right', {})
            if right.get('style') == 'thin':
                borders.right = xlwt.Borders.THIN
            if right.get('color'):
                borders.right_colour = self._color_to_index(right.get('color'))

            top = b.get('top', {})
            if top.get('style') == 'thin':
                borders.top = xlwt.Borders.THIN
            if top.get('color'):
                borders.top_colour = self._color_to_index(top.get('color'))

            bottom = b.get('bottom', {})
            if bottom.get('style') == 'thin':
                borders.bottom = xlwt.Borders.THIN
            if bottom.get('color'):
                borders.bottom_colour = self._color_to_index(bottom.get('color'))

            xlwt_style.borders = borders

        # Обработка выравнивания
        if style.get('alignment'):
            alignment = xlwt.Alignment()
            align = style.get('alignment')

            horz_map = {
                'general': xlwt.Alignment.GENERAL,
                'left': xlwt.Alignment.HORZ_LEFT,
                'center': xlwt.Alignment.HORZ_CENTER,
                'right': xlwt.Alignment.HORZ_RIGHT
            }
            alignment.horz = horz_map.get(align.get('horizontal', 'general'),
                                          xlwt.Alignment.GENERAL)

            vert_map = {
                'bottom': xlwt.Alignment.VERT_BOTTOM,
                'center': xlwt.Alignment.VERT_CENTER,
                'top': xlwt.Alignment.VERT_TOP
            }
            alignment.vert = vert_map.get(align.get('vertical', 'bottom'),
                                          xlwt.Alignment.VERT_BOTTOM)

            alignment.wrap = align.get('wrap_text', False)
            xlwt_style.alignment = alignment

        # Обработка формата чисел
        if style.get('number_format'):
            xlwt_style.num_format_str = style.get('number_format', 'general')
        elif isinstance(style.get('value'), (datetime, date)):
            xlwt_style.num_format_str = 'dd.mm.yyyy'

        return xlwt_style

    def _color_to_index(self, color: str) -> int:
        """Конвертирует hex цвет в индекс xlwt"""
        import xlwt
        # Простая реализация - для сложных случаев нужно использовать палитру
        color_map = {
            '000000': xlwt.Style.colour_map['black'],
            'FFFFFF': xlwt.Style.colour_map['white'],
            'FF0000': xlwt.Style.colour_map['red'],
            '00FF00': xlwt.Style.colour_map['green'],
            '0000FF': xlwt.Style.colour_map['blue'],
        }
        return color_map.get(color.upper(), xlwt.Style.colour_map['black'])

    def add_cell_coords(self, coords: str, value: Union[None, str, float, int, date, datetime],
                        style: Optional[Dict] = None):
        # В xlwt нет прямого доступа по координатам, нужно парсить
        import xlwt
        col_letter = ''.join(filter(str.isalpha, coords.upper()))
        row_num = int(''.join(filter(str.isdigit, coords))) - 1

        # Конвертируем букву столбца в число
        col_num = 0
        for char in col_letter:
            col_num = col_num * 26 + (ord(char) - ord('A') + 1)
        col_num -= 1

        self.add_cell(row_num + 1, col_num + 1, value, style)

    def add_cell(self, row: int, col: int, value: Union[None, str, float, int, date, datetime],
                 style: Optional[Dict] = None):
        if not self.current_worksheet:
            self.select_worksheet('Sheet1')

        # Обработка недопустимых символов
        if isinstance(value, str):
            value = ''.join(c for c in value if c in printable)

        xlwt_style = self._get_style(style)

        # Устанавливаем формат для дат
        if isinstance(value, datetime):
            xlwt_style.num_format_str = 'dd.mm.yyyy hh:mm:ss'
        elif isinstance(value, date):
            xlwt_style.num_format_str = 'dd.mm.yyyy'

        # xlwt использует индексацию с 0
        self.current_worksheet.write(row - 1, col - 1, value, xlwt_style)
        self.rows_qty += 1

    def add_row(self, row: int, list_cells: Iterable[Union[None, str, float, int, date, datetime]],
                start_col: int = 1, styles: Union[None, List, Dict] = None):
        if isinstance(list_cells, dict):
            list_cells_ = list(list_cells.values())
        else:
            list_cells_ = list_cells

        for col, cell in enumerate(list_cells_):
            style = None
            if styles:
                if isinstance(styles, list) and col < len(styles):
                    style = styles[col]
                elif isinstance(styles, dict):
                    style = styles
            self.add_cell(row, start_col + col, cell, style)

    def add_column(self, col: int, list_cells: Iterable[Union[None, str, float, int, date, datetime]],
                   start_row: int = 1, styles: Union[None, List, Dict] = None):
        if isinstance(list_cells, dict):
            list_cells_ = list(list_cells.values())
        else:
            list_cells_ = list_cells

        for row, cell in enumerate(list_cells_):
            style = None
            if styles:
                if isinstance(styles, list) and row < len(styles):
                    style = styles[row]
                elif isinstance(styles, dict):
                    style = styles
            self.add_cell(start_row + row, col, cell, style)

    def add_list_rows(self, first_row: int, first_col: int, list_rows: Iterable[Union[Dict, List]],
                      styles: Union[None, List, Dict] = None):
        rows_cnt = len(list_rows)
        if styles:
            styles_cnt = len(styles)
        else:
            styles_cnt = 0

        for row_index, row_ in enumerate(list_rows):
            if isinstance(row_, dict):
                row = list(row_.values())
            else:
                row = row_

            if isinstance(styles, list) and styles_cnt == rows_cnt:
                self.add_row(first_row + row_index, row, first_col, styles[row_index])
            else:
                self.add_row(first_row + row_index, row, first_col, styles)

    def add_merge_cell(self, first_row: int, first_col: int, last_row: int, last_col: int,
                       value: Union[None, str, float, int, date, datetime], style: Optional[Dict] = None):
        # Добавляем значение в первую ячейку
        self.add_cell(first_row, first_col, value, style)

        # Объединяем ячейки (xlwt использует индексацию с 0)
        self.current_worksheet.write_merge(
            first_row - 1, last_row - 1,
            first_col - 1, last_col - 1,
            value, self._get_style(style)
        )

    def add_merge_cell_coords(self, first_coords: str, last_coords,
                              value: Union[None, str, float, int, date, datetime], style: Optional[Dict] = None):
        # Парсим координаты
        def parse_coords(coords):
            col_letter = ''.join(filter(str.isalpha, coords.upper()))
            row_num = int(''.join(filter(str.isdigit, coords)))

            col_num = 0
            for char in col_letter:
                col_num = col_num * 26 + (ord(char) - ord('A') + 1)

            return row_num, col_num

        first_row, first_col = parse_coords(first_coords)
        last_row, last_col = parse_coords(last_coords)

        self.add_merge_cell(first_row, first_col, last_row, last_col, value, style)

    def set_cell_dimension(self, row: int, col: int, height: Union[int, float] = 15, width: Union[int, float] = 10):
        # Устанавливаем высоту строки
        try:
            # xlwt использует 1/256 ширины символа
            self.current_worksheet.col(col - 1).width = int(width * 256)
        except:
            pass

        try:
            # xlwt использует 1/20 точки для высоты
            self.current_worksheet.row(row - 1).height_mismatch = True
            self.current_worksheet.row(row - 1).height = int(height * 20)
        except:
            pass

    def set_rows_height(self, list_rows_height: Iterable[float], start_row: int = 1):
        for row, height in enumerate(list_rows_height):
            try:
                self.current_worksheet.row(start_row - 1 + row).height_mismatch = True
                self.current_worksheet.row(start_row - 1 + row).height = int(height * 20)
            except:
                pass

    def set_columns_width(self, list_columns_width: Iterable[float], start_col: int = 1):
        for col, width in enumerate(list_columns_width):
            try:
                self.current_worksheet.col(start_col - 1 + col).width = int(width * 256)
            except:
                pass

    def create_simple_excel(self, filename, data: Iterable[Union[Dict, List]], column_width: Optional[Iterable] = None,
                            column_names: Optional[Iterable] = None, styles: Union[None, List, Dict] = None,
                            worksheet: str = 'Sheet', rewrite: bool = True, start_row: int = 1):
        import xlwt

        # Стиль для заголовков
        header_style_dict = {'bold': True, 'border': BORDER.get('bottom')}
        header_style = self._get_style(header_style_dict)

        self.open_file(filename, rewrite)

        if rewrite and 'Sheet1' in self.worksheets:
            self.rename_worksheet('Sheet1', worksheet)
        self.select_worksheet(worksheet)

        if column_width:
            self.set_columns_width(column_width)

        _start_row = start_row

        # Добавляем заголовки
        if column_names:
            for col, value in enumerate(column_names):
                self.current_worksheet.write(_start_row - 1, col, value, header_style)
            _start_row += 1

        # Добавляем данные
        if any(isinstance(e, dict) for e in data):
            data_list = [list(x.values()) for x in data]
        else:
            data_list = data

        for row_index, row_data in enumerate(data_list):
            row_style = None
            if styles:
                if isinstance(styles, list) and row_index < len(styles):
                    row_style = styles[row_index]
                elif isinstance(styles, dict):
                    row_style = styles

            for col_index, value in enumerate(row_data):
                cell_style = None
                if row_style:
                    if isinstance(row_style, list) and col_index < len(row_style):
                        cell_style = row_style[col_index]
                    elif isinstance(row_style, dict):
                        cell_style = row_style

                self.add_cell(_start_row + row_index, col_index + 1, value, cell_style)

        self.save_file()

    def get_max_row(self):
        if not self.current_worksheet:
            return 0
        return self.current_worksheet.nrows

    def get_max_column(self):
        if not self.current_worksheet:
            return 0
        return self.current_worksheet.ncols

    def read_file(self, excel_header: list, sheet_name: str = None,
                  int_columns: list = None, date_columns: list = None, start_row: int = 1):
        import xlrd

        excel_arr = []
        columns = excel_header

        ws = self.worksheets.get(sheet_name, self.current_worksheet)

        # Получаем все строки начиная с start_row
        records = []
        for i in range(start_row - 1, ws.nrows):
            row_values = []
            for j in range(ws.ncols):
                try:
                    row_values.append(ws.cell_value(i, j))
                except:
                    row_values.append(None)
            records.append(row_values)

        int_columns = int_columns if int_columns else []
        date_columns = date_columns if date_columns else []

        for r in records:
            tmp_row = dict(zip(columns, r))

            for c in columns:
                if tmp_row.get(c) is not None:
                    # Обработка целых чисел
                    if c in int_columns and not isinstance(tmp_row.get(c), int):
                        try:
                            tmp_row[c] = int(float(tmp_row[c]))
                        except (ValueError, TypeError):
                            tmp_row[c] = 0

                    # Обработка дат
                    if c in date_columns and not isinstance(tmp_row.get(c), datetime):
                        try:
                            # Пробуем распарсить как строку
                            tmp_row[c] = self._parse_date(str(tmp_row[c]))
                        except (TypeError, ValueError):
                            try:
                                # Обработка числового представления даты в Excel
                                if isinstance(tmp_row[c], float):
                                    tmp_row[c] = datetime(1899, 12, 31) + timedelta(days=tmp_row[c] - 1)
                            except (TypeError, ValueError):
                                tmp_row[c] = None

                    # Обработка строк
                    if c not in date_columns and c not in int_columns and not isinstance(tmp_row.get(c), str):
                        tmp_row[c] = str(tmp_row.get(c))
            excel_arr.append(tmp_row)

        return excel_arr