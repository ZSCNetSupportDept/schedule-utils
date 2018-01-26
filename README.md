# 用来自动化更新值班表的小工具

## User Manual
Needs `openpyxl` to run, to install: `pip install openpyxl`

Run with `./extract.py -h` for help

## Examples
Just print:
```
./extract.py -f print test.xlsx
```

To extract to csv format:
```
./extract.py -f csv test.xlsx
```

To extract to sql-update format:
```
./extract.py -f sql_update test.xlsx
```

## License
WTFPL
