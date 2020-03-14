<?php
    $numAnterior;
    $numAtual = 0;

 public function fibonacci(){
    $numAnterior = $numAtual;
    $numAtual = $numAnterior + $numAtual;
}

while($numAtual <= 30){
    echo(fibonacci());
}