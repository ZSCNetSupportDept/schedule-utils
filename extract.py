from pprint import pprint

from openpyxl import load_workbook, Workbook
from openpyxl.worksheet import Worksheet

from blocks import Block

LEADER_ROW = 32
BLOCK__ROW_MAP = {  # block -> row
    Block.FX: 2,
    Block.BM: 7,
    Block.DM: 12,
    Block.QT: 17,
    Block.XH: 22,
    Block.ZH: 27
}


def extract_staff_name(name: str) -> str:
    return name.split('-')[0].strip()


def extract(filename):
    wb: Workbook = load_workbook(filename=filename)
    ws: Worksheet = wb.active
    schedule = {}
    for week in range(1, 7):
        column = chr(ord('A') + week)
        leader = extract_staff_name(ws[f"{column}{LEADER_ROW}"].value)
        schedule[week] = {
            'leader': leader,
            'staffs': {}
        }
        for block, rowIndex in BLOCK__ROW_MAP.items():
            schedule[week]['staffs'][block] = []
            for i in range(5):
                cell = ws[f"{column}{rowIndex + i}"]
                if cell.value:
                    schedule[week]['staffs'][block].append(extract_staff_name(cell.value))
    return schedule


if __name__ == '__main__':
    pprint(extract('test.xlsx'))
