# 用来自动化更新值班表的小工具

## User Manual
Run with `./extract.py -h` for help

## Examples
To just print (assuming the target file is `test.xlsx`):
```
./extract.py -f print test.xlsx
```

To extract as csv format (assuming the target file is `test.xlsx`):
```
./extract.py -f csv test.xlsx
```

To extract as sql-update format (assuming the target file is `test.xlsx`):
```
./extract.py -f sql_update test.xlsx
```

## License
WTFPL
