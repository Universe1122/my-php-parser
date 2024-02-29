from utils.PhpParserListener import PhpParserListener

class Listener(PhpParserListener):
    def enterEveryRule(self, ctx):
        # print("Rule:", PhpParser.ruleNames[ctx.getRuleIndex()])
        pass

    def exitEveryRule(self, ctx):
        pass

    def visitTerminal(self, node):
        # print("Terminal:", node.symbol.text)
        pass

    def enterEchoStatement(self, node):
        data = node.expressionList()
        # print(dir(data.expression()[0]))
        print("echo param: ", data.expression()[0].getText())
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