<?php
use PhpParser\Node\Scalar\String_ as StringScalar;
use PhpParser\Node\Scalar\Int_ as IntScalar;
use PhpParser\Node\Scalar\Float_ as FloatScalar;
use PhpParser\Node\Expr\FuncCall as FuncCallExpr;
use PhpParser\Node\Expr\Array_ as ArrayExpr;
use PhpParser\Node\Expr\Variable as VariableExpr;
use PhpParser\Node\Expr\ArrayDimFetch as ArrayDimFetchExpr;

class TYPE {
    public static $STRING;
    public static $INT;
    public static $FLOAT;
    public static $FUNC;
    public static $ARRAY;
    public static $VAR;
    public static $ARRAYDIMFETCH;

    public static function initialize() {
        self::$STRING = StringScalar::class;
        self::$INT = IntScalar::class;
        self::$FLOAT = FloatScalar::class;
        self::$FUNC = FuncCallExpr::class;
        self::$ARRAY = ArrayExpr::class;
        self::$VAR = VariableExpr::class;
        self::$ARRAYDIMFETCH = ArrayDimFetchExpr::class;
    }
}

TYPE::initialize();
?>