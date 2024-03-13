from analyzer.structure.type.Function import Function

class FunctionDeclaration:
    def __init__(self, function: Function):
        self.function: Function = function
    
    def getFunction(self) -> Function:
        return self.function