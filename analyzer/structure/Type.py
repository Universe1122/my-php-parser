from enum import Enum

class Variable:
    def __init__(self, name: str):
        self.name = name
        self.type = None
    
    def get(self):
        return self.name

    def toString(self):
        return f"name={self.name}, type={self.type}"

class UnknownVariable:
    def __init__(self, name: str):
        self.name = name
        self.type = None
    
    def get(self):
        return self.name

    def toString(self):
        return f"name={self.name}, type={self.type}"

class NumericNumberConstant:
    def __init__(self, value: str, _type):
        self.value = value
        self.type = _type
    
    def get(self):
        return self.value
    
    def toString(self):
        return f"value={self.value}, type={self.type}"

class RealNumberConstant:
    def __init__(self, value: float):
        self.value = value
        self.type = float
    
    def get(self):
        return self.value
    
    def toString(self):
        return f"value={self.value}, type={self.type}"

class BooleanConstant:
    def __init__(self, value: bool):
        self.value = value
        self.type = bool

    def get(self):
        return self.value
    
    def toString(self):
        return f"value={self.value}, type={self.type}"

class StringConstant:
    def __init__(self, value: str):
        self.value = value
        self.type = str
    
    def get(self):
        return self.value
    
    def toString(self):
        return f"value={self.value}, type={self.type}"

class FunctionConstant:

    def __init__(self, function_name: str):
        self.name = function_name
    
    def get(self):
        return self.name
    
    def toString(self):
        return f"name={self.name}"

class OperatorConstant:
    def __init__(self, operator: str):
        self.operator = operator
        
        if operator == Operator.PLUS.value:
            self.type = Operator.PLUS
        elif operator == Operator.MINUS.value:
            self.type = Operator.MINUS
        elif operator == Operator.MULTIPLY.value:
            self.type = Operator.MULTIPLY
        elif operator == Operator.DIVIDE.value:
            self.type = Operator.DIVIDE
        elif operator == Operator.MODULO.value:
            self.type = Operator.MODULO
        elif operator == Operator.ASSIGN.value:
            self.type = Operator.ASSIGN
        elif operator == Operator.PLUS_ASSIGN.value:
            self.type = Operator.PLUS_ASSIGN
        elif operator == Operator.MINUS_ASSIGN.value:
            self.type = Operator.MINUS_ASSIGN
        elif operator == Operator.MULTIPLY_ASSIGN.value:
            self.type = Operator.MULTIPLY_ASSIGN
        elif operator == Operator.DIVIDE_ASSIGN.value:
            self.type = Operator.DIVIDE_ASSIGN
        elif operator == Operator.MODULO_ASSIGN.value:
            self.type = Operator.MODULO_ASSIGN
        elif operator == Operator.CONCATENATE.value:
            self.type = Operator.CONCATENATE
        elif operator == Operator.CONCATENATE_ASSIGN.value:
            self.type = Operator.CONCATENATE_ASSIGN
        elif operator == Operator.INCREMENT_PREFIX.value:
            self.type = Operator.INCREMENT_PREFIX
        elif operator == Operator.INCREMENT_POSTFIX.value:
            self.type = Operator.INCREMENT_POSTFIX
        elif operator == Operator.DECREMENT_PREFIX.value:
            self.type = Operator.DECREMENT_PREFIX
        elif operator == Operator.DECREMENT_POSTFIX.value:
            self.type = Operator.DECREMENT_POSTFIX
        elif operator == Operator.EQUAL.value:
            self.type = Operator.EQUAL
        elif operator == Operator.IDENTICAL.value:
            self.type = Operator.IDENTICAL
        elif operator == Operator.NOT_EQUAL.value:
            self.type = Operator.NOT_EQUAL
        elif operator == Operator.NOT_IDENTICAL.value:
            self.type = Operator.NOT_IDENTICAL
        elif operator == Operator.GREATER_THAN.value:
            self.type = Operator.GREATER_THAN
        elif operator == Operator.LESS_THAN.value:
            self.type = Operator.LESS_THAN
        elif operator == Operator.GREATER_THAN_OR_EQUAL.value:
            self.type = Operator.GREATER_THAN_OR_EQUAL
        elif operator == Operator.LESS_THAN_OR_EQUAL.value:
            self.type = Operator.LESS_THAN_OR_EQUAL
        elif operator == Operator.LOGICAL_AND.value:
            self.type = Operator.LOGICAL_AND
        elif operator == Operator.LOGICAL_OR.value:
            self.type = Operator.LOGICAL_OR
        elif operator == Operator.LOGICAL_XOR.value:
            self.type = Operator.LOGICAL_XOR
        elif operator == Operator.LOGICAL_AND_ALTERNATE.value:
            self.type = Operator.LOGICAL_AND_ALTERNATE
        elif operator == Operator.LOGICAL_OR_ALTERNATE.value:
            self.type = Operator.LOGICAL_OR_ALTERNATE
        elif operator == Operator.LOGICAL_NOT.value:
            self.type = Operator.LOGICAL_NOT
        elif operator == Operator.ARRAY_PLUS.value:
            self.type = Operator.ARRAY_PLUS
        elif operator == Operator.ARRAY_EQUAL.value:
            self.type = Operator.ARRAY_EQUAL
        elif operator == Operator.ARRAY_IDENTICAL.value:
            self.type = Operator.ARRAY_IDENTICAL
        elif operator == Operator.ARRAY_NOT_EQUAL.value:
            self.type = Operator.ARRAY_NOT_EQUAL
        elif operator == Operator.ARRAY_NOT_EQUAL_ALT.value:
            self.type = Operator.ARRAY_NOT_EQUAL_ALT
        elif operator == Operator.ARRAY_NOT_IDENTICAL.value:
            self.type = Operator.ARRAY_NOT_IDENTICAL
        elif operator == Operator.BITWISE_AND.value:
            self.type = Operator.BITWISE_AND
        elif operator == Operator.BITWISE_OR.value:
            self.type = Operator.BITWISE_OR
        elif operator == Operator.BITWISE_XOR.value:
            self.type = Operator.BITWISE_XOR
        elif operator == Operator.BITWISE_NOT.value:
            self.type = Operator.BITWISE_NOT
        elif operator == Operator.LEFT_SHIFT.value:
            self.type = Operator.LEFT_SHIFT
        elif operator == Operator.RIGHT_SHIFT.value:
            self.type = Operator.RIGHT_SHIFT
        else:
            raise ValueError("Invalid operator")
    
    def get(self):
        return self.operator
    
    def toString(self):
        return f"operator={self.operator}, type={self.type}"

class Operator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    ASSIGN = "="
    PLUS_ASSIGN = "+="
    MINUS_ASSIGN = "-="
    MULTIPLY_ASSIGN = "*="
    DIVIDE_ASSIGN = "/="
    MODULO_ASSIGN = "%="
    CONCATENATE = "."
    CONCATENATE_ASSIGN = ".="
    INCREMENT_PREFIX = "++"
    INCREMENT_POSTFIX = "++"
    DECREMENT_PREFIX = "--"
    DECREMENT_POSTFIX = "--"
    EQUAL = "=="
    IDENTICAL = "==="
    NOT_EQUAL = "!="
    NOT_IDENTICAL = "!=="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN_OR_EQUAL = "<="
    LOGICAL_AND = "and"
    LOGICAL_OR = "or"
    LOGICAL_XOR = "xor"
    LOGICAL_AND_ALTERNATE = "&&"
    LOGICAL_OR_ALTERNATE = "||"
    LOGICAL_NOT = "!"
    ARRAY_PLUS = "+"
    ARRAY_EQUAL = "=="
    ARRAY_IDENTICAL = "==="
    ARRAY_NOT_EQUAL = "!="
    ARRAY_NOT_EQUAL_ALT = "<>"
    ARRAY_NOT_IDENTICAL = "!=="
    BITWISE_AND = "&"
    BITWISE_OR = "|"
    BITWISE_XOR = "^"
    BITWISE_NOT = "~"
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"

class TypeDeclarations(Enum):
    CLASS_NAME = "CLASS"
    INTERFACE_NAME = "INTERFACE"
    SELF = "SELF"
    PARENT = "PARENT"
    ARRAY = "ARRAY"
    CALLABLE = "CALLABLE"
    BOOL = "BOOL"
    FLOAT = "FLOAT"
    INT = "INT"
    STRING = "STRING"
    NULLABLE = "NULLABLE"
    VOID = "VOID"
    ITERABLE = "ITERABLE"