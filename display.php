<?php
function main(array $args) : array {
    $number = $args["number"];
    $doubled = $args["doubled"];
    return ["result" => $doubled, "original"=> $number];
}

