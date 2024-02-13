<?php
require __DIR__ . '/../vendor/autoload.php';
use PhpParser\{Error, NodeVisitorAbstract, NodeTraverser, Node};
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

include __DIR__ . "/../visitor/Visitor.php";
include __DIR__ . "/../config.php";

$code = <<<'CODE'
<?php

$data = $_GET["test"];
echo $data;

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