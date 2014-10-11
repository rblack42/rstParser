from rstparser.rst.Parser import Parser

def main():
    print 'rstParser...'
    parser = Parser()
    text = open('tests/data/test.rst').readlines()
    parser.parse(text)
