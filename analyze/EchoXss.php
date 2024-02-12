<?php
    class EchoXss {
        public $variable;
        public $echo;

        public function __construct($variable, $echo) {
            $this->variable = $variable;
            $this->echo = $echo;

            $this->analyze();
        }

        public function analyze() {
            foreach($this->echo->variable as $var) {
                if($this->variable->variable[$var]["type"] == PhpParser\Node\Scalar\String_::class){
                    echo "123";
                }
            }
        }
    }
?>