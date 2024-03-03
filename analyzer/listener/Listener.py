from utils.PhpParser import PhpParser
from utils.PhpParserListener import PhpParserListener
from analyzer.structure.DataFlow import *
from analyzer.structure.Type import *
from analyzer.analyzer import *

class Listener(PhpParserListener):
    def __init__(self):
        self.variables = DataFlow()

    def enterEveryRule(self, ctx):
        # print("Rule:", PhpParser.ruleNames[ctx.getRuleIndex()])
        pass

    def exitEveryRule(self, ctx):
        pass

    def visitTerminal(self, node):
        # print("Terminal:", node.symbol.text)
        pass

    def enterEchoStatement(self, ctx:PhpParser.EchoStatementContext):
        echoStatement(ctx.expressionList().expression())
        # print(ctx.expressionList().expression()[0].children)
        # data = node.expressionList()
        # print(dir(data.expression()[0]))
        # print("echo param: ", data.expression()[0].getText())
        # print("enterEchoStatement: ", node.expressionList())
    
    def enterFunctionCall(self, node): 
        pass
        # print(dir(node.functionCallName()))
        # print(node.functionCallName().getText())
        # print(dir(node))
        # print(dir(node.actualArguments()))
        # if node.arguments() is not None:
        #     arguments = [arg.getText() for arg in node.arguments().actualArgument()]
        #     print("Arguments:", arguments)

    def enterAssignmentExpression(self, ctx: PhpParser.AssignmentExpressionContext):
        if not ctx.assignable():
            print("[!] Not found variable name")
            pass
        
        var_name: str = ctx.assignable().getText()

        expression = assignmentExpression(ctx.expression().getChildren())
        self.variables.addNode(var_name = var_name, expression = expression)
        # self.variables.show()
        # print("===== expression ======")
        # for exp in expression:
        #     print(exp.get())
        # print("=======================")