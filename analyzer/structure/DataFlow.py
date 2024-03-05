from analyzer.structure.Type import *

class Node:
    def __init__(self, name: str, expression: list):
        self.name: str = name
        self.expression = expression
        self.next: Node = None
        self.type = None
    
    def getName(self):
        return self.name

    def getExpression(self):
        return self.expression
    
    def getNext(self):
        return self.next
    
    def getType(self):
        return self.type

class DataFlow:
    def __init__(self):
        self.root = list()
    
    def addNode(self, var_name: str, expression: list):
        """
        변수를 추적하기 위해, 변수 정보를 추가하는 함수
        - 새로운 변수인 경우, root 변수에 Node 객체를 생성하여 저장
        - 기존에 존재하는 변수인 경우, findNode() 함수로 해당 변수의 node를 찾고, 해당 node의 next 맴버 변수에 새로운 Node 객체를 저장
        - expression 안에 변수가 존재하는지 확인하기 위해 expressionReference() 함수로 확인
        """

        node = self.findNode(var_name = var_name) 
        expression = self.expressionReference(expression = expression)
        new_node = Node(name = var_name, expression = expression)

        if node == None:
            new_node.type = self.__guessType(new_node)
            self.root.append(new_node)
        else:
            last_node = self.getLastNode(node)
            new_node.type = self.__guessType(new_node)
            last_node.next = new_node
    
    def findNode(self, var_name: str) -> Node:
        """
        변수 이름(var_name)을 가진 node를 찾는 함수
        """
        for node in self.root:
            if node.getName() == var_name:
                return node
        
        return None

    def expressionReference(self, expression: list) -> list:
        """
        expression 안에 변수 정보가 존재하는 경우, 해당 변수의 마지막 상태 값을 링크하기 위한 기능
        만약, 존재하지 않는 변수인 경우 UnknownVariable 객체를 생성하여 expression 안에 저장
        """
        return_data = list()

        for exp in expression:
            if isinstance(exp, Variable):
                var_name = exp.getName()

                node = self.findNode(var_name = var_name)

                if node == None:
                    ## TODO
                    ## 변수 ref 를 찾지 못했지만, 일단 push
                    print("[!] Not found Variable Reference: ", exp)
                    return_data.append(UnknownVariable(name = var_name))
                    continue
                
                last_node = self.getLastNode(node)
                exp.link_node = last_node
                return_data.append(exp)

            elif isinstance(exp, Array):
                return_data.append(Array(expression=self.expressionReference(exp.getExpression())))
            
            elif isinstance(exp, Function):
                return_data.append(Function(func_name=exp.getName(), expression=self.expressionReference(exp.getExpression())))

            else:
                print(f"[!] expressionReference: else -> Unexpected Type: {type(exp)}")
                return_data.append(exp)
        
        return return_data

    def getLastNode(self, node: Node) -> Node:
        """
        node 변수의 마지막 상태 변경 node를 찾는 함수
        """
        last_node = node

        while last_node.getNext() != None:
            last_node = last_node.getNext()
        
        return last_node

    def findExpressionReference(self, target_node: Node, find_node: Node) -> list:
        count = 0
        
        while target_node != find_node and target_node.getNext() != None:
            target_node = target_node.getNext()
            count += 1
        
        if target_node == find_node:
            return [count, target_node]
        else:
            return [None, None]
    
    def __guessType(self, var: Variable):
        _types = list()

        for exp in var.getExpression():
            if isinstance(exp, NumericNumberConstant):
                _types.append(TypeDeclarations.INT)
            elif isinstance(exp, RealNumberConstant):
                _types.append(TypeDeclarations.FLOAT)
            elif isinstance(exp, RealNumberConstant):
                _types.append(TypeDeclarations.BOOL)
            elif isinstance(exp, StringConstant):
                _types.append(TypeDeclarations.STRING)
            elif isinstance(exp, Function):
                _types.append(TypeDeclarations.CALLABLE)
            elif isinstance(exp, OperatorConstant):
                _types.append(exp.type)
            elif isinstance(exp, Array):
                _types.append(exp.type)
            elif isinstance(exp, Variable):
                _types.append(exp.link_node.type)
            elif isinstance(exp, UnknownVariable):
                _types.append(None)
        
        if Operator.CONCATENATE in _types or TypeDeclarations.STRING in _types:
            return TypeDeclarations.STRING
    
        elif TypeDeclarations.ARRAY in _types:
            return TypeDeclarations.ARRAY
        
        elif Operator.PLUS in _types or \
                Operator.MINUS in _types or \
                Operator.MULTIPLY in _types or \
                Operator.DIVIDE in _types or \
                Operator.MODULO in _types:
            return TypeDeclarations.INT


        elif TypeDeclarations.INT in _types or TypeDeclarations.FLOAT in _types:
            return TypeDeclarations.INT
        
        elif TypeDeclarations.BOOL in _types:
            return TypeDeclarations.BOOL
        
        elif TypeDeclarations.CALLABLE in _types:
            ## TODO
            ## 함수 선언부에서 어떤 값을 리턴하는지 확인해야 함
            print("[!] __guessType():CALLABLE -> return None")
            return TypeDeclarations.CALLABLE
        
        else:
            print("[!] __guessType():ELSE -> return None")
            return None

    def show(self):
        import json

        def toStringExpression(expression: list):
            return_expression = list()

            for exp in expression:
                if isinstance(exp, Variable):
                    target_node = self.findNode(exp.getName())
                    find_expression_ref_node = self.findExpressionReference(target_node=target_node, find_node=exp.link_node)
                    
                    return_expression.append({
                        "index" : find_expression_ref_node[0],
                        "type" : str(type(exp)),
                        "name" : exp.getName(),
                        "expression" : toStringExpression(find_expression_ref_node[1].getExpression())
                    })

                elif isinstance(exp, Array):
                    return_expression.append({
                        "type" : str(exp.type),
                        "expression" : toStringExpression(exp.getExpression())
                    })
                
                elif isinstance(exp, Function):
                    return_expression.append({
                        "name" : exp.getName(),
                        "type" : str(exp.type),
                        "expression" : toStringExpression(exp.getExpression())
                    })

                else:
                    return_expression.append({
                        "type" : str(type(exp)),
                        "toString" : exp.toString()
                    })

            return return_expression

        for node in self.root:
            print(f"Variable Name: {node.getName()}")
            print(f"type: {node.getType()}")
            print(f"expression: ", json.dumps(toStringExpression(node.getExpression()), indent=4))

            next_node = list()
            tmp_node = node
            while tmp_node.getNext() != None:
                tmp_node = tmp_node.getNext()
                next_node.append({
                    "name" : tmp_node.getName(),
                    "expression" : toStringExpression(tmp_node.getExpression()),
                    "type" : str(tmp_node.type)
                })

            print(f"next: ", json.dumps(next_node, indent=4))
            print("\n")