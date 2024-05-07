# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock
from stock import Stock
from fileparse import parse_csv
import tableformat


def read_portfolio(filename):
    with open(filename) as lines:
        portfoliodict = parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portfoliodict]
    return portfolio


def read_prices(filename1):
    with open(filename1) as lines:
        prices = dict(parse_csv(lines, types = [str, float], has_headers = False))
        return prices

def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    #print('%10s %10s %10s %10s' % headers)
    #print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def construct_report(portfolio, prices):
    report = []
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        rowesque = (stock.name, stock.shares, prices[stock.name], change)
        report.append(rowesque)
    return report

        
def portfolio_report(filename, filename1, fmt = 'txt'):
    portfolio = read_portfolio(filename)
    prices = read_prices(filename1)
    report = construct_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter);


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage : %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
