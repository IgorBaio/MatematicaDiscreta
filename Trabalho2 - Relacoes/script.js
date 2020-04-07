function getMyProgram(){
 var file1 = prompt("digite o diretorio do arquivo 1: "); 
 file1 = getFile1(file1);
 var file2 = prompt("digite o diretorio do arquivo 2: "); 
file2 = getFile1(file2);
var a = file1+","+file2
 document.write(a);


}

function getFile1(file){
    var arquivo = open(file.value);
    return arquivo;
    // document.write(file1);
    // var file1 = document.getElementById(id1);
    // var file2 = document.getElementById("file1");
    // file2 = open(file2.value);
    // document.write(file1+file2)

    // var file2 = document.getElementById(id2);
    // file2 = open(file2.value);
    // document.write(file2);


    // var file1  = window.File
}