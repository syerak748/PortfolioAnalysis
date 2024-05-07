class TableFormatter:
    def headings(self, headers):
        '''
        emit table headers
        '''
        raise NotImplementedError()
    def row(self, rowdata):
        '''
        emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''table in plain text format'''
    def headings(self, headings):
        for h in headings:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-'*10+' ')*len(headings))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end = ' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print('<th>',h,'</th>',sep = '', end = '')
        print('/tr>')

    def row(self, rowdata):
        print('<tr>', end = '')
        for r in rowdata:
            print('<td>',r,'</td>',sep = '', end = '')
        print('/tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Invalid format type {name}')

def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
    
                   
        
