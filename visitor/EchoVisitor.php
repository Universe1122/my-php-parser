<?php

class EchoVisitor {
    public $nodes;
    public $variable;

    public function __construct(array $nodes) {
        $this->nodes = $nodes;
        $this->variable = array();

        foreach($nodes as $node) {
            if($node instanceof PhpParser\Node\Stmt\Echo_){
                foreach($node->exprs as $expr) {
                    $this->echoFunctionParsing($expr);
                }
            }
        }
    }

    public function echoFunctionParsing($expr) {
        /*
            스칼라 (문자열, 숫자 등): PhpParser\Node\Scalar
                                            PhpParser\Node\Scalar\String_: 문자열 값
                                            PhpParser\Node\Scalar\LNumber: 정수 값
                                            PhpParser\Node\Scalar\DNumber: 부동 소수점 수 값
                                            PhpParser\Node\Scalar\Encapsed: 복합 문자열 값 (변수를 포함할 수 있는 문자열)
                                            PhpParser\Node\Scalar\MagicConst: 매직 상수 (예: __LINE__, __FILE__ 등)
                                            PhpParser\Node\Scalar\EncapsedStringPart: 복합 문자열의 일부분
                                            PhpParser\Node\Scalar\StringPart: 문자열의 일부분
            이항 연산자: PhpParser\Node\Expr\BinaryOp\Concat
            변수: PhpParser\Node\Expr\Variable
            함수: PhpParser\Node\Expr\FuncCall
            메서드: PhpParser\Node\Expr\MethodCall 
                ex) testobj->testfunc()
            정적 메서드: PhpParser\Node\Expr\StaticCall
                ex) MyClass::staticMethodName()
            클래스: 
    
        */
        // if($expr instanceof PhpParser\Node\Scalar\String_) {
        //     echo $expr->value . "\n";
        // }
    
        // else if ($expr instanceof PhpParser\Node\Expr\BinaryOp\Concat) {
        //     if($expr->left){
        //         echoFunctionParsing($expr->left);
        //     }
        //     if($expr->right){
        //         echoFunctionParsing($expr->right);
        //     }
        // }
    
        // else if ($expr instanceof PhpParser\Node\Expr\Variable) {
        //     echo $expr->name . "\n";
        // }
    
        // else {
        //     echo "[!] unexpected instance: " . get_class($expr) . "\n";
        // }
    
        if ($expr instanceof PhpParser\Node\Expr\Variable) {
            array_push($this->variable, $expr->name);
        }
    
        else if ($expr instanceof PhpParser\Node\Expr\BinaryOp\Concat) {
            if($expr->left){
                $this->echoFunctionParsing($expr->left);
            }
            if($expr->right){
                $this->echoFunctionParsing($expr->right);
            }
        }
    }
}
?>