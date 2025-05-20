from enum import Enum
from colorama import Cursor, Fore, Style, init

init(autoreset=True)

def print_error(message):
    print(Fore.RED + message)

def print_success(message):
    print(Fore.GREEN + message)

def print_title(message):
    print(Style.BRIGHT + message)

def print_header(message):
    print(Fore.BLUE + message)

class Table():
    index_column_width = 8

    class RowType(Enum):
        SINGLE_LINE = 1
        DOULBLE_LINE = 2

    def __init__(self, headers, widths, keys,
                 alignments=None, formats=None, index=False, x_offset=0, y_offset=0):

        self.headers = headers
        self.widths = widths
        self.keys = keys
        self.alignments = alignments if alignments else ["<"] * len(headers)
        self.formats = formats if formats else [""] * len(headers)
        self.index = index
        self.x_offset = x_offset
        self.y_offset = y_offset

    def offset_x(self):
        if self.x_offset:
            print(Cursor.FORWARD(self.x_offset), end="")
    def offset_y(self):
        if self.y_offset:
            print(Cursor.UP(self.y_offset), end="")


    def single_line(self):
        self.offset_x()
        print("--------------------------------------------")

    def double_line(self):
        self.offset_x()
        print("============================================")

    def print(self, array):
        self.offset_x()
        self.offset_y()

        # Print header
        if self.index:
            print(f"{'Index':<{self.index_column_width}}", end="")

        for i in range(len(self.headers)):
            print(f"{self.headers[i]:<{self.widths[i]}}", end="")
        print()

        self.single_line()

        # Print pies
        for row, item in enumerate(array):
            if item == Table.RowType.SINGLE_LINE:
                self.single_line()
            elif item == Table.RowType.DOULBLE_LINE:
                self.double_line()
            else:
                self.offset_x()
                if self.index:
                    print(f"{item.get("index", row + 1)
                          :<{self.index_column_width}}", end="")
                for i, key in enumerate(self.keys):
                    value = item.get(key, "")
                    print(f"{value:{self.alignments[i]}{
                          self.widths[i]}{self.formats[i]}}", end="")
                print()

        self.double_line()

        table_height = len(array) + 3

        if table_height < self.y_offset:
            print(Cursor.DOWN(self.y_offset - table_height))
        return table_height
