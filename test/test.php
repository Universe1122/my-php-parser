<?php

    function func($data) {
        $data = 1;
        return $data;
    }

    $data = 1;

    if($data){
        echo "123";
    }
    else {
        func($data);
    }

?>