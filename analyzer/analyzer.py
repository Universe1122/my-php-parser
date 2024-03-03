from utils.PhpParser import PhpParser
from analyzer.structure.Type import *
from antlr4.tree.Tree import *

def assignmentExpression(data: list):
    expression = []
    for child in data:
        if isinstance(child, PhpParser.ConstantContext):
            if child.literalConstant() != None:
                literal = child.literalConstant()

                ## 실수 type
                if literal.Real() != None:
                    data = literal.Real().getText()
                    expression.append(RealNumberConstant(float(data)))
                
                ## boolean type
                elif literal.BooleanConstant() != None:
                    data = literal.BooleanConstant().getText()
                    expression.append(BooleanConstant(bool(data)))

                ## 숫자 type
                elif literal.numericConstant() != None:
                    data = literal.numericConstant()

                    if data.Octal() != None:
                        expression.append(NumericNumberConstant(data.Octal().getText(), oct))
                    elif data.Decimal() != None:
                        expression.append(NumericNumberConstant(data.Decimal().getText(), int))
                    elif data.Hex() != None:
                        expression.append(NumericNumberConstant(data.Hex().getText(), hex))
                    elif data.Binary() != None:
                        expression.append(NumericNumberConstant(data.Binary().getText(), bin))
                    else:
                        print("[!] Unknown literal type")
                        
                ## 문자열 type
                elif literal.stringConstant() != None:
                    expression.append(StringConstant(data.stringConstant().getText()))
                else:
                    print("[!] Unknown literal Type")

            elif child.classConstant() != None:
                ## TODO
                pass
            elif child.magicConstant() != None:
                ## TODO
                pass
            
            else:
                print("[!] Unknown Constant Type")
        
        elif isinstance(child, PhpParser.StringContext):
            ## TODO
            ## 이렇게 getText() 함수만 처리해도 되나?
            data = child.getText()
            data = data[1 : len(data) - 1]
            expression.append(StringConstant(data))
        
        elif isinstance(child, PhpParser.ChainExpressionContext):
            for chain_child in child.chain().chainOrigin().getChildren():
                
                if isinstance(chain_child, PhpParser.ChainBaseContext):
                    for variable in chain_child.keyedVariable():
                        expression.append(Variable(variable.getText()))
                elif isinstance(chain_child, PhpParser.FunctionCallContext):
                    ## TODO
                    ## 함수 호출일 때, getText() 로 함수 이름만 가져와도 되나?
                    expression.append(FunctionConstant(chain_child.getText()))
        
        elif isinstance(child, PhpParser.ChainContext):
            superglobals = ['$GLOBALS', '$_SERVER', '$_GET', '$_POST', '$_FILES', '$_COOKIE', '$_SESSION', '$_REQUEST', '$_ENV']

            for var in child.chainOrigin().chainBase().keyedVariable():
                for child in var.getChildren():
                    if isinstance(child, TerminalNodeImpl):
                        
                        if child.getText() in superglobals:
                            ## TODO
                            ## $_GET[$test], int($_GET["test"]) 이런 경우 구현
                            expression.append(Variable(var.getText()))
                        else:
                            expression.append(Variable(var.getText()))
                    

            # expression.append(Variable(child.getText()))
            # print(child.chainOrigin().chainBase().keyedVariable()[0].children[1].getText())

        elif isinstance(child, PhpParser.ScalarExpressionContext):
            if child.string() != None:
                data = child.getText()
                data = data[1 : len(data) - 1]
                expression.append(StringConstant(data))

            elif child.constant() != None:
                expression.extend(assignmentExpression([child.constant()]))
        
        elif isinstance(child, TerminalNodeImpl):
            expression.append(OperatorConstant(child.getText()))

        else:
            print("[!] Unknown child Type: ", type(child))
    
    return expression

def echoStatement(expression: list):
    parsed_expression = list()
    for exp in expression:

        parsed_expression = assignmentExpression(exp.getChildren())
    

