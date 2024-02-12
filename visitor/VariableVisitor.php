<?php

require __DIR__ . '/../vendor/autoload.php';
use PhpParser\NodeDumper;

class VariableVisitor {
    public $dumper;
    public $variable;
    public $nodes;
    
    public function __construct(array $nodes) {
        $this->dumper = new NodeDumper();
        $this->variable = array();
        $this->nodes = $nodes;

        foreach($nodes as $node) {
            if($node instanceof PhpParser\Node\Stmt\Expression){
                // echo $this->dumper->dump($node->expr);
                $variable_name = $node->expr->var->name;
                // $value = $node->expr->expr->value;
                $value = $this->valueParser($node->expr->expr);

                $this->variable[$variable_name] = $value;
            }
        }
    }

    public function valueParser($expr){
        // echo $this->dumper->dump($expr) . "\n";
        echo get_class($expr) . "\n";

        if($expr instanceof PhpParser\Node\Scalar\String_ || 
            $expr instanceof PhpParser\Node\Scalar\Int_ ||
            $expr instanceof PhpParser\Node\Scalar\Float_) {
            return array(
                "value" => $expr->value,
                "type" => get_class($expr)
            );
        }

        // TODO
        // 함수 등,,

        return array();
    }

    // public function parseVariable($expr)
}
?>