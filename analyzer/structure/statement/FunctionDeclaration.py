from analyzer.structure.type import Function

class FunctionDeclaration:
    def __init__(self):
        self.function: Function = None

    def setFunction(self, function: Function):
        self.function = function
    
    def getFunction(self) -> Function:
        return self.function