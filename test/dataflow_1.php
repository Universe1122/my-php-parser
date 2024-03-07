<?php
    // 일반적인 상황
    $a_000 = "a";
    $a_001 = 1;
    $a_002 = 3.14;
    $a_003 = true;

    // 변수 변화 추적
    $b_000 = "A";
    $b_000 = 1;

    // 변수에 변수 저장
    $c_000 = "a";
    $c_001 = $c_000;
    $c_002 = $c_001 . "a";

    // 연산자
    $d_000 = "a" . "b";
    $d_001 = 1 + 2;
    $d_002 = "a" . test();

    // 커스텀 함수
    $e_000 = test();
    $e_001 = test(1, "a");
    $e_002 = test(1, test(1, "a"));
    $e_003 = test($a_000);
    $e_004 = test(1, test(1, $a_000));
    $e_005 = test(array(1));

    // array and Associative Array
    $f_000 = array(1);
    $f_001 = array("a");
    $f_002 = array(1, "a");
    $f_003 = array(1, array(1, "a"));
    $f_004 = array($a_000);
    $f_005 = array("a" => 123);
    $f_006 = array("a" => array(1));

    // superglobal
    $g_000 = $_GET["test"]["a"];

?>