
var calc = () =>{

    var a = document.forms["input_form"]["avalue"].value;
    var b = document.forms["input_form"]["bvalue"].value;
    var c = document.forms["input_form"]["cvalue"].value;
    var output = document.getElementById('output');
    
    if (a == 0) {
        outputText = "Cant be zero";
    } else if (isNaN(a)) {
        outputText = "must be a number";
    } else if (isNaN(b)) {
        outputText = "must be a number";
    } else if (isNaN(c)) {
        outputText = "must be a number";
    } else {
        var x1 = (-(b/2*a) + Math.sqrt((Math.pow((b/2*a),2))-(c/a))); 
        var x2 = (-(b/2*a) - Math.sqrt((Math.pow((b/2*a),2))-(c/a))); 
        var outputText = 'The first value of x is ' + x1 + ' and the second is '+ x2;
    }
    
    document.getElementById("output_text").innerHTML = outputText;
}