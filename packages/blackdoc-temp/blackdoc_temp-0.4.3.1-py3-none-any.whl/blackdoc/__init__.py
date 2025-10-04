from blackdoc.blacken import blacken
from blackdoc.classification import detect_format
from blackdoc.formats import InvalidFormatError, register_format  # noqa: F401

__version__ = "0.4.3.1"


def line_numbers(lines):
    yield from enumerate(lines, start=1)


def format_lines(lines, mode=None):
    numbered = line_numbers(lines)

    labeled = detect_format(numbered)
    blackened = blacken(labeled, mode=mode)

    return blackened
