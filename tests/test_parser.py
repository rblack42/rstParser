import unittest

class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def test_parser(self):
        from rstparser.rst.Parser import Parser
        parser = Parser()
        text = open('tests/data/test.rst').readlines()
        parser.parse(text)
        self.assertEqual(1, 1)

