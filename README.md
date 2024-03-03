# my-php-parser

TODO
- array, superglobal 등 아래와 같은 경우 처리하기

```php
<?php
    $array = array(1, "2"); 
    $array[0] = "1";

    $data = $_GET["aaa"];
    $data = $_GET[$data];
    $data = int($_GET["aaa"]);
    $_GET["aaa"] = "1";
?>
```

- 함수 리턴값 파악하기
- echo 함수 호출 시, 인자들 분석해서 xss 가능한지 확인하기
- xss 방지 함수가 있는지 확인하기
- custom xss 방지 함수는 설정 파일 등으로 사용자가 입력하게끔 하기
- 