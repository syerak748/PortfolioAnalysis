import os
import time


def follow(filename):
    f = open('Data/stocklog.csv')
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line
        

    
if __name__ == '__main__':
    import report
    portfolio = report.read_portfolio('/Users/rxnkshitij748/practical-python/Work/Data/portfolio.csv')
    for line in follow('/Users/rxnkshitij748/practical-python/Work/Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

