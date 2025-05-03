from enum import Enum
class RowType(Enum):
    SINGLE_LINE = 1
    DOULBLE_LINE = 2
# pie information stored in one array
pies = [
    {"name": "Apple Pie", "price": 10},
    {"name": "Cherry Pie", "price": 12},
    {"name": "Blueberry Pie", "price": 15},
    {"name": "Pumpkin Pie", "price": 8},
    {"name": "Pecan Pie", "price": 14},
    {"name": "Lemon Meringue Pie", "price": 11},
    {"name": "Key Lime Pie", "price": 13},
    {"name": "Chocolate Cream Pie", "price": 9},
    {"name": "Banana Cream Pie", "price": 16},
    {"name": "Butter Chicken Pie", "price": 7}
]

class Table():
    index_column_width = 8
    def __init__(self, headers, widths, keys, alignments=None, formats=None, index=False):
        self.headers = headers
        self.widths = widths
        self.keys = keys
        self.alignments = alignments if alignments else ["<"] * len(headers)
        self.formats = formats if formats else [""] * len(headers)
        self.index = index

    def single_line(self):
        print("--------------------------------------------")

    def double_line(self):
        print("============================================")

    def print(self, array):
        # Print header
        if self.index:
            print(f"{'Index':<{self.index_column_width}}", end="")

        for i in range(len(self.headers)):
            print(f"{self.headers[i]:<{self.widths[i]}}", end="")
        print()
        self.single_line()

        # Print pies
        for row, item in enumerate(array):
            if item == RowType.SINGLE_LINE:
                self.single_line()
            elif item == RowType.DOULBLE_LINE:
                self.double_line()
            else:
                if self.index:
                    print(f"{item.get("index", row + 1):<{self.index_column_width}}", end="")
                for i, key in enumerate(self.keys):
                    value = item.get(key, "")
                    print(f"{value:{self.alignments[i]}{self.widths[i]}{self.formats[i]}}", end="")
                print()

        self.double_line()



