"""Handler functions, return a brief summary of a value."""
import datetime

def summarize_str(inp):
    """AAAA"""
    return inp


def summarize_float(inp):
    """AAAA"""
    return str(inp)


def summarize_int(inp):
    """AAAA"""
    return str(inp)


def summarize_dict(inp):
    """Return an empty string for a dictionary"""
    return ""


def summarize_datetime(inp):
    """AAAA"""
    return inp.strftime("%Y-%m-%d %H:%M:%S")


def summarize_date(inp):
    """AAAA"""
    return inp.strftime("%Y-%m-%d")


def summarize_list(inp):
    """AAAA"""

    if len(inp) < 10:
        return str(inp)
    else:
        return str([min(inp), max(inp)])
