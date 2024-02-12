<?php
require __DIR__ . '/../vendor/autoload.php';
use PhpParser\{Error, NodeVisitorAbstract, NodeTraverser, Node};
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

class EchoVisitor extends NodeVisitorAbstract {
    public $variable = array();

    public function beforeTraverse(array $nodes) {}
    public function leaveNode(Node $node) {}
    public function enterNode(Node $node) {}
    public function afterTraverse(array $nodes) {
        foreach($nodes as $node) {
            if($node instanceof PhpParser\Node\Stmt\Echo_){
                foreach($node->exprs as $expr) {
                    echoFunctionParsing($expr);
                }
            }
        }
    }
}

function echoFunctionParsing($node) {
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

    */
    if($node instanceof PhpParser\Node\Scalar\String_) {
        echo $node->value . "\n";
    }

    else if ($node instanceof PhpParser\Node\Expr\BinaryOp\Concat) {
        if($node->left){
            echoFunctionParsing($node->left);
        }
        if($node->right){
            echoFunctionParsing($node->right);
        }
    }

    else if ($node instanceof PhpParser\Node\Expr\Variable) {
        echo $node->name . "\n";
    }

    else {
        echo "[!] unexpected instance: " . get_class($node) . "\n";
    }
}

?>