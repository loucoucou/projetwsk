<?php
function main(array $args) : array {
    $number = $args["number"] ?? 0;
    $doubled = $number * 2;
    return ["number" => $number, "doubled" => $doubled];
}

