"""
The braille lookup table takes alpha numeric
characters and converts them to 6bit information
"""

_braille_lookup = {
    'a': 0b100000,
    'b': 0b101000,
    'c': 0b110000,
    'd': 0b110100,
    'e': 0b100100,
    'f': 0b111000,
    'g': 0b111100,
    'h': 0b101100,
    'i': 0b011000,
    'j': 0b011100,
    'k': 0b100010,
    'l': 0b101010,
    'm': 0b110010,
    'n': 0b110110,
    'o': 0b100110,
    'p': 0b111010,
    'q': 0b111110,
    'r': 0b101110,
    's': 0b011010,
    't': 0b011110,
    'u': 0b100011,
    'v': 0b101011,
    'w': 0b011101,
    'x': 0b110011,
    'y': 0b110111,
    'z': 0b100111,
}


def braille_lookup(char: str) -> int:
    return _braille_lookup[char]
