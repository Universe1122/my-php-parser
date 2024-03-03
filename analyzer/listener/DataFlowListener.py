from utils.PhpParserListener import PhpParserListener
from utils.PhpParser import PhpParser

from analyzer.structure.DataFlow import *

class DataFlowListener(PhpParserListener):
    def __init__(self):
        self.variables = list()

    def enterAssignmentExpression(self, ctx:PhpParser.AssignmentExpressionContext):
        # print(type(ctx.assignmentOperator()))
        # print(dir(ctx.assignmentOperator()))
        
        ## 이거는 변수에 값을 할당하기 위해 사용하는 oprator가 뭔지 알 수 있는 기능임
        ## 예를 들어, $x = 1; 이면 = 이 operator 값임
        # print(ctx.assignmentOperator().PlusEqual())

        # expression = ctx.expression()
        print(ctx.children[0].getText())

        for token in ctx.children:
            ## 변수 이름
            if type(token) is PhpParser.AssignableContext: 
                self.variables.append(Node(token.getText()))
            
            # elif type(token) is Php

        # if type(expression) is PhpParser.ScalarExpressionContext:
            
        
        # elif type(expression) is PhpParser.ArithmeticExpressionContext:
        #     pass

    # def enterVariable(self, ctx: PHPParser.VariableContext):
    #     pass