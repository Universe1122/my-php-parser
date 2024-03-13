from antlr4 import *

from utils.PhpLexer import PhpLexer
from utils.PhpParser import PhpParser
from analyzer.structure.Type import *
from analyzer.listener.Listener import Listener
from analyzer.listener.DataFlowListener import DataFlowListener
from config import log

class Analyzer:
    
    def __init__(self, filename: str):
        self.filename = filename
        self.models = list()
    
    def start(self):
        input_stream = FileStream(self.filename, encoding='utf-8')
        lexer = PhpLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PhpParser(stream)
        tree = parser.htmlDocument()

        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        listener.result["file"] = self.filename
        self.models.append(listener.result)

def assignmentExpression(data: list):
    expression = []
    for child in data:
        if isinstance(child, PhpParser.ConstantContext):
            
            if child.literalConstant() != None:
                """
                $data = 3.14;
                $data = "test";
                $data = true;
                """

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
            """
            $data = "test";
            """

            ## TODO
            ## 이렇게 getText() 함수만 처리해도 되나?
            data = child.getText()
            data = data[1 : len(data) - 1]
            expression.append(StringConstant(data))
        
        elif isinstance(child, PhpParser.ChainExpressionContext) or \
             isinstance(child, PhpParser.ChainContext):
            """
            $data = test() . "asdf";

            $data = $x;
            $data = $_GET["asdf"];
            $data = func();
            """

            superglobals = ['$GLOBALS', '$_SERVER', '$_GET', '$_POST', '$_FILES', '$_COOKIE', '$_SESSION', '$_REQUEST', '$_ENV']

            if isinstance(child, PhpParser.ChainExpressionContext):
                child = child.chain()
            
            for _child in child.chainOrigin().getChildren():
                
                if isinstance(_child, PhpParser.FunctionCallContext):
                    expression.append(__functionParser(_child))
                
                if isinstance(_child, PhpParser.ChainBaseContext):
                    for __child in _child.keyedVariable():
                        if __child.VarName():
                            var_name = __child.VarName().getText()

                            if var_name in superglobals:
                                """
                                $test = $_GET["test1"]["test2"];
                                """
                                _expression = list()
                                for data in __child.squareCurlyExpression():
                                    _expression.extend(assignmentExpression([data.expression()]))
                                
                                expression.append(SuperGlobals(name=var_name, expression=_expression))
                            else:
                                expression.append(__VariableParser(__child.VarName()))
                        else:
                            print("[!] VarName이 없는 상황 발생: ")
                            
            # superglobals = ['$GLOBALS', '$_SERVER', '$_GET', '$_POST', '$_FILES', '$_COOKIE', '$_SESSION', '$_REQUEST', '$_ENV']

            # for var in child.chainOrigin().chainBase().keyedVariable():
            #     for child in var.getChildren():
            #         if isinstance(child, TerminalNodeImpl):
                        
            #             if child.getText() in superglobals:
            #                 ## TODO
            #                 ## $_GET[$test], int($_GET["test"]) 이런 경우 구현
            #                 expression.append(Variable(var.getText()))
            #             else:
            #                 expression.append(Variable(var.getText()))
                    

            # expression.append(Variable(child.getText()))
            # print(child.chainOrigin().chainBase().keyedVariable()[0].children[1].getText())

        elif isinstance(child, PhpParser.ScalarExpressionContext):
            """
            $data = "test" . "asdf";
            """

            if child.string() != None:
                data = child.getText()
                data = data[1 : len(data) - 1]
                expression.append(StringConstant(data))

            elif child.constant() != None:
                expression.extend(assignmentExpression([child.constant()]))
        
        elif isinstance(child, TerminalNodeImpl):
            """
            +
            -
            /
            """

            expression.append(OperatorConstant(child.getText()))
        
        elif isinstance(child, PhpParser.ArrayCreationContext):
            """
            $data = array(1,2);
            """

            _expression = list()

            for _child in child.arrayItemList().getChildren():
                if isinstance(_child, PhpParser.ArrayItemContext):

                    if _child.getChildCount() == 3:
                        """
                        dict 형태인 경우
                        array("a" => 1)
                        """
                        tmp = list()
                        tmp.extend(assignmentExpression(_child.expression()))

                        _expression.append(AssociativeArray({tmp[0] : tmp[1]}))

                    elif _child.getChildCount() == 1:
                        """
                        list 형태인 경우
                        array(1, 2)
                        """
                        _expression.extend(assignmentExpression(_child.expression()))

                    else:
                        print("[!] Array 파싱 시, child 길이 예외 발생: ", _child.getChildCount())

                else:
                    print("[!] Array 파싱 시, 타입 예외 발생: ", type(_child))
            
            new_array = Array(expression=_expression)
            expression.append(new_array)

        elif isinstance(child, PhpParser.ArrayCreationExpressionContext):
            """
            $data = array(1,array(1));
            """
            
            expression.extend(assignmentExpression([child.arrayCreation()]))

        else:
            print("[!] Unknown child Type: ", type(child))
    
    return expression

def echoStatement(ctx):
    tmp_exp = list()

    if isinstance(ctx, PhpParser.ParenthesisExpressionContext):
        tmp_exp.extend(echoStatement(ctx.parentheses()))
    elif isinstance(ctx, PhpParser.ArithmeticExpressionContext):
        """
        echo "123" . "123";
        """
        tmp_exp.extend(assignmentExpression(ctx.getChildren()))
    elif isinstance(ctx, PhpParser.ParenthesesContext):
        tmp_exp.extend(echoStatement(ctx.expression()))
    else:
        tmp_exp.extend(assignmentExpression([ctx]))
        
    return tmp_exp
    

def __functionParser(ctx: PhpParser.FunctionCallContext) -> Function:
    """
    이 함수는 assignmentExpression() 함수에서 FunctionCallContext 타입일 때 호출된다.
    외부에서 이 함수를 호출할 목적으로 만들어진 것이 아니다.
    """

    func_name = ""
    _expression = list()

    for child in ctx.getChildren():

        if isinstance(child, PhpParser.FunctionCallNameContext):
            func_name = child.getText()

        elif isinstance(child, PhpParser.ActualArgumentsContext):
            for arguments in child.arguments():
                for argument in arguments.actualArgument():
                    _expression.extend(assignmentExpression(argument.getChildren()))
        else:
            print("[!] Unknown Type in FunctionCallContext: ", type(child))
    
    return Function(func_name=func_name, expression=_expression)


def __VariableParser(ctx):
    return Variable(ctx.getText())