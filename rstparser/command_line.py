from rstparser.rst import Parser

def main():
    print 'rstParser...'
    parser = Parser()
    text = open('tests/data/test.rst').read()
    ast = parser.parse(text, 'document')
    print ast
