document.getElementById("number-1").addEventListener("click", addNumber1);
document.getElementById("number-2").addEventListener("click", addNumber2);
document.getElementById("number-3").addEventListener("click", addNumber3);
document.getElementById("number-4").addEventListener("click", addNumber4);
document.getElementById("number-5").addEventListener("click", addNumber5);
document.getElementById("number-6").addEventListener("click", addNumber6);
document.getElementById("number-7").addEventListener("click", addNumber7);
document.getElementById("number-8").addEventListener("click", addNumber8);
document.getElementById("number-9").addEventListener("click", addNumber9);
document.getElementById("number-0").addEventListener("click", addNumber0);


document.getElementById("delete").addEventListener("click", deleteNumber);


var digital_number = document.getElementById("digital_number");
var number_box = document.getElementById("number_box");
var number = "";

function addNumber(){
    digital_number.innerHTML = "";
    if (number != 0) {
        digital_number.innerHTML = number;
        number_box.setAttribute("value", number);
    }
    else{
        digital_number.innerHTML = "0";
        number_box.setAttribute("value", "0");
    }
    
}


function addNumber1(){
    number += "1";
    addNumber();
}
function addNumber2(){
    number += "2";
    addNumber();
}
function addNumber3(){
    number += "3";
    addNumber();
}
function addNumber4(){
    number += "4";
    addNumber();
}
function addNumber5(){
    number += "5";
    addNumber();
}
function addNumber6(){
    number += "6";
    addNumber();
}
function addNumber7(){
    number += "7";
    addNumber();
}
function addNumber8(){
    number += "8";
    addNumber();
}
function addNumber9(){
    number += "9";
    addNumber();
}
function addNumber0(){
    number += "0";
    addNumber();
}

function deleteNumber(){
    digital_number.innerHTML = "0";
    number = "";
    number_box.setAttribute("value", "0");
}