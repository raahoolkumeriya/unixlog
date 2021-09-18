from typing import Dict
from colorama import Fore, Style
from functools import wraps
from datetime import datetime

COLOR_DICT = {
        'warning': Fore.LIGHTYELLOW_EX,
        'error': Fore.LIGHTRED_EX,
        'success': Fore.LIGHTGREEN_EX,
        'debug': Fore.LIGHTCYAN_EX,
        'info': Fore.LIGHTBLUE_EX,
        'trace': Fore.LIGHTMAGENTA_EX
    }

def assign_time():
    """Get latest time stamp value"""
    return datetime.strftime(datetime.now(), format='%Y-%m-%d %T')


def apply_color(mode: str, text: str):
    """
    Common function for applying color like unix style

    Attributes
    ----------
    mode (str): string
    text (str): string

    Returns
    -------
    str
    """
    timestamp = assign_time()
    return f"{timestamp} {COLOR_DICT.get(mode)} {text} {Style.RESET_ALL}"


def center_filler(f):
    @wraps(f)
    def wrapper(*args):
        return apply_color(f.__name__, f'[{f.__name__.upper().center(9)}] ' + args[0])
    return wrapper


@center_filler
def warning(text):
    """
    Warning Function with Yellow Color texted retrun string
    """
    return text

@center_filler
def error(text):
    """
    Error Function with Red Color texted retrun string
    """
    return text

@center_filler
def info(text):
    """
    Info Function with Blue Color texted retrun string
    """
    return text
    

@center_filler
def success(text):
    """
    Success Function with Green Color texted retrun string
    """
    return text
    

@center_filler
def debug(text):
    """
    Debug Function with Cyan Color texted retrun string
    """
    return text
    

@center_filler
def trace(text):
    """
    Trace Function with Magenta Color texted retrun string
    """
    return text
