class FunctionParameter:
    def __init__(self, parameter_name: str):
        self.name: str = parameter_name
        self.type = None
    
    def getName(self):
        return self.name

    def setType(self, _type):
        self.type = _type
    
    def getType(self):
        return self.type
