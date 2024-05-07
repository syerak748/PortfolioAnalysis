import csv
import sys
import report
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0;
    '''with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                total_cost = total_cost + int(record['shares'])*float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Couldn\'t Convert: {row}')
    return total_cost;'''
    portfolio = read_portfolio(filename)
    for row in portfolio:
        total_cost += row.shares*row.price
    return total_cost

'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'
totalcost = portfolio_cost(filename)
print("total_cost : ", totalcost)'''
        
