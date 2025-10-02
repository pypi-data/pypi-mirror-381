from string import printable
from typing import Union, Optional, List, Dict, Iterable
from datetime import datetime, timedelta, date

BORDER_NONE = {
    'left': {
        'style': None,
        'color': 'FFFFFFFF'
    },
    'right': {
        'style': None,
        'color': 'FFFFFFFF'
    },
    'bottom': {
        'style': None,
        'color': 'FFFFFFFF'
    },
    'top': {
        'style': None,
        'color': 'FFFFFFFF'
    },
}

BORDER_BLACK_LINE = {
    'style': 'thin',
    'color': '000000'
}

BORDER = {
    'none': BORDER_NONE,
    'all': {
        'left': BORDER_BLACK_LINE,
        'right': BORDER_BLACK_LINE,
        'bottom': BORDER_BLACK_LINE,
        'top': BORDER_BLACK_LINE,
    },
    'left': {
        **BORDER_NONE,
        'left': BORDER_BLACK_LINE,
    },
    'right': {
        **BORDER_NONE,
        'right': BORDER_BLACK_LINE,
    },
    'bottom': {
        **BORDER_NONE,
        'bottom': BORDER_BLACK_LINE,
    },
    'top': {
        **BORDER_NONE,
        'top': BORDER_BLACK_LINE,
    }
}

FONT = {
    'default': {
        'name': 'Calibri',
        'size': 11,
        'bold': False,
        'italic': False,
        'underline': 'none',
        'strike': False,
        'color': '000000'
    }
}

NUMBER_FORMAT = {
    'date': {'number_format': 'dd.mm.yyyy'},
    'datetime': {'number_format': 'dd.mm.yyyy hh:mm:ss'},
    'other': {'number_format': 'general'}
}