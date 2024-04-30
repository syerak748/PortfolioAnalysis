# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimit = ',', silence_errors = False):
    if select and not has_headers:
            raise RuntimeError("select argument requires colum headers")
        
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimit)
        
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows,1):
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno} : Couldnt convert {row}")
                        print(f"Row {rowno} : Reason {e}")
                    continue
                    
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
        
