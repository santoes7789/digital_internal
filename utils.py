from enum import Enum
from colorama import Cursor, Fore, Style, init

init(autoreset=True)
# Wrapper functions for print:
# Error is red text
# Sucess is green text
# Title is bolded text
# Header is blue text
def print_error(message):
    print(Fore.RED + message)

def print_success(message):
    print(Fore.GREEN + message)

def print_title(message):
    print(Style.BRIGHT + message)

def print_header(message):
    print(Fore.BLUE + message)

# Class for table template which can be printed
class Table():
    index_column_width = 8

    class RowType(Enum):
        SINGLE_LINE = 1
        DOULBLE_LINE = 2

    def __init__(self, headers, widths, keys,
                 alignments=None, formats=None, index=False, x_offset=0, y_offset=0):

        # Headers to be put at the top of table
        self.headers = headers

        # Widths of each column
        self.widths = widths

        # Keys for accessing dictionary elements
        self.keys = keys

        # Formattinng options for alignment and formats
        self.alignments = alignments if alignments else ["<"] * len(keys)
        self.formats = formats if formats else [""] * len(keys)

        # Boolean whether index should be shown
        self.index = index

        # Offsetting table so it can be printed anywhere (relative to current cursor position)
        self.x_offset = x_offset
        self.y_offset = y_offset

    # Functions to apply offset
    def offset_x(self):
        if self.x_offset:
            print(Cursor.FORWARD(self.x_offset), end="")

    def offset_y(self):
        if self.y_offset:
            print(Cursor.UP(self.y_offset), end="")

    # Prints single or double line with offset
    def single_line(self):
        self.offset_x()
        print("--------------------------------------------")

    def double_line(self):
        self.offset_x()
        print("============================================")

    # Print the table given an array
    def print(self, array):
        # Set offset
        self.offset_y()

        # Print header
        if self.headers:
            # Set x offset
            self.offset_x()

            # Print index header if index is true
            if self.index:
                print(f"{'Index':<{self.index_column_width}}", end="")

            # Print other headers
            for index, header in enumerate(self.headers):
                print(f"{header:<{self.widths[index]}}", end="")
            print()

        self.single_line()

        # Print pies, by iterating through each itemS
        for row, item in enumerate(array):
            # If item is a single or double line, print that
            if item == Table.RowType.SINGLE_LINE:
                self.single_line()
            elif item == Table.RowType.DOULBLE_LINE:
                self.double_line()

            # Else print the row out
            else:
                self.offset_x()
                # Print index column if index is true
                if self.index:
                    element = item.get("index", row + 1)
                    print(f"{element:<{self.index_column_width}}", end="")

                # Iterate through each key, and getting value,
                # printing with proper alignment, width and format
                for i, key in enumerate(self.keys):
                    value = item.get(key, "")
                    print(f"{value:{self.alignments[i]}{self.widths[i]}{self.formats[i]}}", end="")
                print()

        # Ending double line to show end of table
        self.double_line()

        # Calculate table height
        table_height = len(array) + 3

        # Put the cursor back to where it was previously
        if table_height < self.y_offset:
            print(Cursor.DOWN(self.y_offset - table_height))

        # Return table height
        return table_height
