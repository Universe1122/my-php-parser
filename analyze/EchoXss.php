<?php

class EchoXss {
    public $variable_parser;
    public $echo_parser;

    public function __construct($variable_parser, $echo_parser) {
        $this->variable_parser = $variable_parser;
        $this->echo_parser = $echo_parser;

        $this->analyze();
    }

    public function analyze() {
        foreach($this->echo_parser->variable as $var) {
            $var = $this->variable_parser->variable[$var];
            
            if($var["type"] === TYPE::$ARRAYDIMFETCH){
                // special variable 이면 일단 탐지
                if (in_array($var["value"]["key"], $this->variable_parser->super_global)) {
                    echo "XSS 가능\n"; 
                }
            }
        }
    }
}
?>