<?php
require __DIR__ . '/../vendor/autoload.php';
use PhpParser\{Error, NodeVisitorAbstract, NodeTraverser, Node};
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

include __DIR__ . "/EchoVisitor.php";
include __DIR__ . "/VariableVisitor.php";
include __DIR__ . "/../analyze/EchoXss.php";

class Visitor extends NodeVisitorAbstract {
    public $variable = array();

    public function beforeTraverse(array $nodes) {}
    public function leaveNode(Node $node) {}
    public function enterNode(Node $node) {}
    public function afterTraverse(array $nodes) {
        $variable_visitor = new VariableVisitor($nodes);
        $echo_visitor = new EchoVisitor($nodes);
        // echo "\n\n";
        // print_r($variable_visitor->variable);
        // print_r($variable_visitor->variable["data6"]["value"][0]);
        new EchoXss($variable_visitor, $echo_visitor); 
    }
}
?>