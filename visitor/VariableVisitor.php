<?php

require __DIR__ . '/../vendor/autoload.php';
use PhpParser\NodeDumper;

class VariableVisitor {
    public $dumper;
    public $variable;
    public $nodes;
    public $super_global;
    
    public function __construct(array $nodes) {
        $this->dumper = new NodeDumper();
        $this->variable = array();
        $this->nodes = $nodes;
        // https://www.php.net/manual/en/language.variables.superglobals.php
        $this->super_global = array(
            "\$GLOBALS", // => TODO, 이거 어떻게 처리해야 할지
            "\$_SERVER",
            "\$_GET",
            "\$_POST",
            "\$_FILES",
            "\$_COOKIE",
            "\$_SESSION",
            "\$_REQUEST",
            "\$_ENV"
        );

        foreach($nodes as $node) {
            if($node instanceof PhpParser\Node\Stmt\Expression){
                $this->parse($node->expr);
                echo $this->dumper->dump($node->expr) . "\n";
                // $variable_name = $node->expr->var->name;
                // // $value = $node->expr->expr->value;
                // $value = $this->valueParser($node->expr->expr);

                // $this->variable[$variable_name] = $value;
            }
        }
    }

    public function parse($expr) {
        // echo $this->dumper->dump($expr) . "\n";
        $var_name = $this->parseVariableName($expr->var);
        $var_value = $this->parseVariableType($expr->expr);
        $this->variable[$var_name] = $var_value;
    }

    public function parseVariableName($var) {
        /*
            변수의 이름을 가져오는 함수

            parameter:
                $var: 
                    var: Expr_Variable(
                        name: data1
                    )
        
            return
                type: String
        */
        // echo get_class($var) . "\n";
        if($var instanceof PhpParser\Node\Expr\Variable){
            return $var->name;
        }
        
        echo "[parseVariableName] Unexpected type: " . get_class($var);
        exit();
    }

    public function parseVariableType($expr) {
        /*
            변수의 값을 추측하고, 그에 맞는 파싱 함수를 호출하는 함수

            parameter: 
                $expr:
                    expr: Expr_Variable(
                        name: data1
                    )
            
            return:
                type: TODO
        */

        if($expr instanceof PhpParser\Node\Scalar\String_) {
            return array(
                "value" => $this->parseString($expr),
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Scalar\Int_) {
            return array(
                "value" => $this->parseInt($expr),
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Scalar\Float_) {
            return array(
                "value" => $this->parseFloat($expr),
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Expr\FuncCall){
            return array(
                "value" => $this->parseFunctionCall($expr),
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Expr\Array_) {
            // Example
            // $data6 = array(1,"test" => 1,3);

            $result = array();
            
            foreach($expr->items as $item) {
                // key가 있는 경우
                // TODO
                // 여기 에러나는거 해결하기
                if($item->key !== null) {
                    array_push($result, array(
                        $item->key => $this->parseVariableType($item->value)
                    ));
                }

                // key가 없는 경우
                else{
                    array_push($result, $this->parseVariableType($item->value));
                }
            }

            return array(
                "value" => $result,
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Expr\Variable) {
            // Example
            // $data3 = $data1

            return array(
                "value" => $this->parseVariableName($expr),
                "type" => get_class($expr)
            );
        }

        if($expr instanceof PhpParser\Node\Expr\ArrayDimFetch) {
            $result = array();
            $tmp_node = $expr;
            $tmp_dim = array();

            do {
                array_unshift($tmp_dim, $this->parseVariableType($tmp_node->dim));
                $tmp_node = $tmp_node->var;
            } while($tmp_node instanceof PhpParser\Node\Expr\ArrayDimFetch);

            $var_name = $this->parseVariableName($tmp_node);

            return array(
                "value" => array(
                    "key" => $var_name,
                    "dim" => $tmp_dim
                ),
                "type" => get_class($expr)
            );
        }


        echo "[parseVariableType] Unexpected type: " . get_class($expr) . "\n";
        return "";
    }

    public function parseString($expr) {
        return $expr->value;
    }

    public function parseInt($expr) {
        return $expr->value;
    }

    public function parseFloat($expr) {
        return $expr->value;
    }

    public function parseFunctionCall($expr){
        // TODO 
        // 함수의 리턴 값을 변수에 넣고 있는데, 이건 어떻게 처리해야 할지,,
        return "TODO: functionCall";
    }    

    // public function valueParser($expr){
    //     // TODO
    //     // 리커시브하게 이 함수를 호출할건데, 리턴 형태를 재정의 해야 할듯
    //     echo $this->dumper->dump($expr) . "\n";
    //     // echo get_class($expr) . "\n";

    //     if($expr instanceof PhpParser\Node\Scalar\String_ || 
    //         $expr instanceof PhpParser\Node\Scalar\Int_ ||
    //         $expr instanceof PhpParser\Node\Scalar\Float_) {
    //         return array(
    //             "value" => $expr->value,
    //             "type" => get_class($expr)
    //         );
    //     }

    //     if($expr instanceof PhpParser\Node\Expr\FuncCall){
    //         // TODO
    //         // 함수 리턴 값이 변수에 들어갈 때, 이를 처리하는 로직 추가하기
    //         return array(
    //             "value" => "TODO",
    //             "type" => get_class($expr)
    //         );
    //     }

    //     if($expr instanceof PhpParser\Node\Expr\Array_) {
    //         // echo $this->dumper->dump($expr->items) . "\n";
    //         // echo get_class($expr->items[0]) . "\n";
    //         // var_dump($expr->items);
    //         return array(
    //             "value" => "TODO",
    //             "type" => get_class($expr)
    //         );  
    //     }

    //     if($expr instanceof PhpParser\Node\Expr\ArrayDimFetch) {

    //     }


    //     echo "[valueParser] Unexpected type: " . get_class($expr) . "\n";
    //     return array();
    // }
}
?>