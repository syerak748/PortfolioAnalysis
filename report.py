# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(zip(headers, row))
            holding['name'] = holding['name']
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)
    return portfolio

def read_prices(filename1):
    prices = {}
    with open(filename1) as f1:
        rows1 = csv.reader(f1)
        for row in rows1:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue

    return prices
'''
portfoliofile = "/Users/rxnkshitij748/practical-python/Work/Data/portfolio.csv"
pricesfile = "/Users/rxnkshitij748/practical-python/Work/Data/prices.csv"
portfolio = read_portfolio(portfoliofile) #list of dictionaries
prices = read_prices(pricesfile) #dictionaries with stock name : value
portfolio_value_ini = 0.0
portfolio_value_final = 0.0
for stock in portfolio:
    name = stock['name']
    shares = stock['shares']
    price = stock['price']
    pricenow = prices[name]
    portfolio_value_ini += shares*price
    portfolio_value_final += shares*pricenow

gain_loss = portfolio_value_final - portfolio_value_ini
if (gain_loss<0):
    print(-1*gain_loss, "is the loss")
else:
    print(gain_loss, "is the profit")
'''
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def construct_report(portfolio, prices):
    report = []
    headers = ('Name', 'Shares', 'Price', 'Change')
    separators = '';
    for stock in portfolio:
        change = prices[stock['name']] - stock['price']
        tuple = (stock['name'], stock['shares'], prices[stock['name']], change)
        report.append(tuple)
    return report

        
def portfolio_report(filename, filename1):
    portfolio = read_portfolio(filename)
    prices = read_prices(filename1)
    report = construct_report(portfolio, prices)
    print_report(report);


    
