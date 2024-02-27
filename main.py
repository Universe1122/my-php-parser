from antlr4 import *
from utils.PhpLexer import PhpLexer
from utils.PhpParser import PhpParser
# from VisitorInterp import VisitorInterp
import sys
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = PhpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PhpParser(stream)
    tree = parser.start_()
    print(tree)

if __name__ == '__main__':
    main(sys.argv)