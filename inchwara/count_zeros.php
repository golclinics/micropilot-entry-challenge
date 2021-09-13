<?php

$array = array(7,2,1,0,1,0,3,9,0);

$value_to_count = 0;

function CountZeros($value_to_count,$array){
    $counts = array_count_values($array);

    return $counts[$value_to_count];
}