from analyzer.structure.type.FunctionParameter import FunctionParameter

class Function:
    def __init__(self, func_name: str, parameter: list[FunctionParameter]):
        self.name: str = func_name
        self.parameter: list[FunctionParameter] = parameter
        self.body: list = None
        self.return_type = None

    def getName(self):
        return self.name
    
    def getParameter(self) -> list[FunctionParameter]:
        return self.parameter