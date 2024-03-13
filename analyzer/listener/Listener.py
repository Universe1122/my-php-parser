from utils.PhpParser import PhpParser
from utils.PhpParserListener import PhpParserListener
from analyzer.structure.DataFlow import *
from analyzer.structure.type.Function import Function
from analyzer.structure.type.FunctionParameter import FunctionParameter
from analyzer.structure.statement.declare.FunctionDeclaration import FunctionDeclaration
from config import log

class Listener(PhpParserListener):
    def __init__(self):
        self.result = {
            "model" : []
        }
    
    def enterTopStatement(self, ctx:PhpParser.TopStatementContext):
        for statement in ctx.getChildren():

            if isinstance(statement, PhpParser.FunctionDeclarationContext):
                new_function_declaration = FunctionDeclaration(self.__FunctionAnalyzer(statement))
                self.result["model"].append(new_function_declaration)

            elif isinstance(statement, PhpParser.StatementContext):
                for _ctx in statement.getChildren():
                    """
                    if, for 등등 statement가 있음
                    """
                    if isinstance(_ctx, PhpParser.ExpressionStatementContext):
                        for __ctx in _ctx.getChildren():
                            if isinstance(__ctx, PhpParser.AssignmentExpressionContext):
                                pass

            else:
                log.warning("[!] Unexpected instance: ", type(statement))

    def __FunctionAnalyzer(self, ctx:PhpParser.FunctionDeclarationContext) -> Function:
        function_name: str = ctx.identifier().getText()
        parameter_info = list()

        ## Get function's parameter
        ## TODO Get parameter's default value if exist
        if ctx.formalParameterList():
            for parameter in ctx.formalParameterList().formalParameter():
                if parameter.variableInitializer():
                    name = parameter.variableInitializer().VarName().getText()
                    parameter_info.append(FunctionParameter(parameter_name=name))
    
        ## TODO Guess return type

        ## TODO Body Parser
                    
        return Function(func_name=function_name, parameter=parameter_info)

    # def enterEveryRule(self, ctx):
    #     # print("Rule:", PhpParser.ruleNames[ctx.getRuleIndex()])
    #     pass

    # def exitEveryRule(self, ctx):
    #     pass

    # def visitTerminal(self, node):
    #     # print("Terminal:", node.symbol.text)
    #     pass

    # def enterEchoStatement(self, ctx:PhpParser.EchoStatementContext):
    #     echo_arguments = list()
    #     for exp in ctx.expressionList().expression():
    #         echo_arguments.extend(echoStatement(exp))
        
    #     print(echo_arguments)
    #     xss = Xss.Xss(self.variables, echo_arguments)
    #     print(xss.echoXss())

    #     # print(ctx.expressionList().expression()[0].children)
    #     # data = node.expressionList()
    #     # print(dir(data.expression()[0]))
    #     # print("echo param: ", data.expression()[0].getText())
    #     # print("enterEchoStatement: ", node.expressionList())
    
    # def enterFunctionCall(self, node): 
    #     pass
    #     # print(dir(node.functionCallName()))
    #     # print(node.functionCallName().getText())
    #     # print(dir(node))
    #     # print(dir(node.actualArguments()))
    #     # if node.arguments() is not None:
    #     #     arguments = [arg.getText() for arg in node.arguments().actualArgument()]
    #     #     print("Arguments:", arguments)

    # def enterAssignmentExpression(self, ctx: PhpParser.AssignmentExpressionContext):
    #     if not ctx.assignable():
    #         print("[!] Not found variable name")
    #         pass
        
    #     var_name: str = ctx.assignable().getText()

    #     expression = assignmentExpression(ctx.expression().getChildren())
    #     self.variables.addNode(var_name = var_name, expression = expression)
    #     # self.variables.show()
    #     # print("===== expression ======")
    #     # for exp in expression:
    #     #     print(exp.get())
    #     # print("=======================")