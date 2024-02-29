from antlr4 import *
from utils.PhpLexer import PhpLexer
from utils.PhpParser import PhpParser

from analyzer.listener.Listener import Listener
from analyzer.listener.DataFlowListener import DataFlowListener
import sys

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = PhpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PhpParser(stream)
    tree = parser.htmlDocument()

    listener = Listener()
    data_flow_listenr = DataFlowListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    walker.walk(data_flow_listenr, tree)

if __name__ == '__main__':
    main(sys.argv)