<?php
require __DIR__ . '/../vendor/autoload.php';
use PhpParser\{Error, NodeVisitorAbstract, NodeTraverser, Node};
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

include __DIR__ . "/../visitor/Visitor.php";

$code = <<<'CODE'
<?php

function test() {};

$data0 = $_GET;
$data1 = $_POST["asdf"];
$data2 = $data[1][2];
$data3 = $data1;
$data4 = "asdf";
$data5 = 1;
$data6 = 2.1;
$data7 = test();
$data8 = array(1, "test" => array("test" => 1));
$data9 = array(1,2,3);
// echo "var: " . $var;
CODE;

$parser = (new ParserFactory())->createForNewestSupportedVersion();
try {
    $ast = $parser->parse($code);
} catch (Error $error) {
    echo "Parse error: {$error->getMessage()}\n";
    return;
}

$traverser = new NodeTraverser();
$traverser->addVisitor(new Visitor());

$traverser->traverse($ast);