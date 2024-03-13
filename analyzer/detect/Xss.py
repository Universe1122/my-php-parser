from analyzer.structure import DataFlow, Type

class Xss:

    def __init__(self, variables: DataFlow, arguments: list):
        self.variables: DataFlow = variables
        self.arguments: list = arguments
    
    def echoXss(self):
        check = 0
        for argument in self.arguments:
            if argument.type == Type.Operator.CONCATENATE:
                check = 1
                break
        
        # if check == 0:
        #     return False
        
        for argument in self.arguments:
            if argument.taint == True:
                return True
        
        return False