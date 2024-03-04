from antlr4 import *
from antlr4.tree.Trees import Trees
from utils.PhpLexer import PhpLexer
from utils.PhpParser import PhpParser

from analyzer.listener.Listener import Listener
from analyzer.listener.DataFlowListener import DataFlowListener
import sys

def main(argv):
    # input_stream = FileStream(argv[1])
    input_stream = FileStream("test/dataflow_1.php")
    lexer = PhpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PhpParser(stream)
    tree = parser.htmlDocument()

    # print(tree.toStringTree())
    # print_tree(tree)
    # print(prettify_lisp_string(Trees.toStringTree(tree, None, parser)))
    # exit()

    listener = Listener()
    data_flow_listenr = DataFlowListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    listener.variables.show()
    # walker.walk(data_flow_listenr, tree)

def print_tree(node, indent=0):
    if node is None:
        return
    
    # 들여쓰기 추가
    print("    " * indent, end="")

    # 노드 유형에 따라 다르게 출력
    if hasattr(node, 'symbol'):  # 토큰 노드인 경우
        print(node.symbol.text)
    elif hasattr(node, 'children'):  # 규칙 노드인 경우
        print(type(node).__name__)
        for child in node.children:
            print_tree(child, indent + 1)

def prettify_lisp_string(lisp_string):
    indent = 0
    prettified_string = ""

    for char in lisp_string:
        if char == "(":
            prettified_string += "\n" + "  " * indent + char
            indent += 1
        elif char == ")":
            indent -= 1
            prettified_string += char
        else:
            prettified_string += char

    return prettified_string

if __name__ == '__main__':
    main(sys.argv)