# MIT License

# Copyright (c) 2024 Turun ammatti-instituutti

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import msvcrt
import ctypes
from ctypes import c_long, c_ulong, c_wchar_p, c_void_p

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

def read():
    """
    Read a key from the keyboard and return it's integer value of the character.
    Some keys have 2 codes in which case this function should be invoked a second time
    to read the second code.
    
    :return: the code of the pressed key. 
    :rtype: int
    """

    return ord(msvcrt.getch())   

def readch():
    """
    Read a key from the keyboard and return it's unicode string representation.
    Some keys have 2 codes in which case this function should be invoked a second time
    to read the second code unicode representation.

    :return: a character representing the code of the pressed key. 
    :rtype: string
    """
    
    return msvcrt.getch().decode("utf-8")

def write(string, line = None, column = None):
    """
    Write a string in the terminal. If no poision is specified using the line and column 
    parameters, the text is displayed at the current cursor position.

    :param string: the text to write in the terminal
    :type string: string
    :param line: line position in the terminal where to write the text
    :type line: int
    :param column: column position in the terminal where to write the text
    :type column: int
    """

    if line != None and column != None:
        move(line, column)

    ctypes.windll.kernel32.WriteConsoleW(gHandle, c_wchar_p(string), c_ulong(len(string)), c_void_p(), None)

def clear():
    """
    Clear the terminal and set cursor to top/left corner.
    """

    move(0, 0)
    terminal_size = os.get_terminal_size()
    write(" " * (terminal_size.columns * terminal_size.lines))
    move(0, 0)

def size():
    """
    Gets the current size of the terminal.
    
    :return: a dictionary with lines and columns fields specifying the size of the terminal. 
    :rtype: dict
    """
    
    return os.get_terminal_size()

def move(line, column):
    """
    Move cursor to position indicated by x and y.

    :param line: line position in the terminal where to move the cursor
    :type line: int
    :param column: column position in the terminal where to move the cursor
    :type column: int
    """

    value = column + (line << 16)
    ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))

"""
NOTE: The special keys always provide 2 codes, so two executions of read() function
are required and the actual key code is provided by the second execution.
The first execution on read() provides either 0 or 224, depending on the machine.
"""

KEY_UP = 72
KEY_DOWN = 80
KEY_LEFT = 75
KEY_RIGHT = 77
