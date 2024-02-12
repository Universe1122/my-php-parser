<?php
require __DIR__ . '/vendor/autoload.php';
use PhpParser\{Error, NodeVisitorAbstract, NodeTraverser, Node};
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;

include __DIR__ . "/visitor/EchoVisitor.php";

$code = <<<'CODE'
<?php

$var = "test";
echo "var: " . $var;
CODE;

$parser = (new ParserFactory())->createForNewestSupportedVersion();
try {
    $ast = $parser->parse($code);
} catch (Error $error) {
    echo "Parse error: {$error->getMessage()}\n";
    return;
}

$traverser = new NodeTraverser();
$traverser->addVisitor(new EchoVisitor());



$traverser->traverse($ast);
// echo $dumper->dump($ast) . "\n";

// foreach($ast as $stmt) {
//     if($stmt instanceof PhpParser\Node\Stmt\Echo_){
//         foreach($stmt->exprs as $expr){
//             echo get_class($expr->left->left->left);
//             echo "\n";
//         }
//     }
// }