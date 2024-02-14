<?php
use PhpParser\Node\Scalar\String_ as StringScalar;
use PhpParser\Node\Scalar\Int_ as IntScalar;
use PhpParser\Node\Scalar\Float_ as FloatScalar;
use PhpParser\Node\Expr\FuncCall as FuncCallExpr;
use PhpParser\Node\Expr\Array_ as ArrayExpr;
use PhpParser\Node\Expr\Variable as VariableExpr;
use PhpParser\Node\Expr\ArrayDimFetch as ArrayDimFetchExpr;

class TYPE {
    public static $String;
    public static $Int;
    public static $Float;
    public static $Func;
    public static $Array;
    public static $Variable;
    public static $ArrayDimFetch;

    public static function initialize() {
        self::$String = StringScalar::class;
        self::$Int = IntScalar::class;
        self::$Float = FloatScalar::class;
        self::$Func = FuncCallExpr::class;
        self::$Array = ArrayExpr::class;
        self::$Variable = VariableExpr::class;
        self::$ArrayDimFetch = ArrayDimFetchExpr::class;
    }
}

TYPE::initialize();
?>