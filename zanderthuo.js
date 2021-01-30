const getX = (a,b,c) => {

    var firstResult = (-1*b + Math.sqrt(Math.pow(b,2) - (4 * a * c))) / (2 * a);
    var secondResult = (-1*b - Math.sqrt(Math.pow(b,2) - (4 * a * c))) / (2 * a);

    if (firstResult > secondResult) {
        console.log(`${firstResult} is greater than ${secondResult}`);
    } else if(secondResult > firstResult){
        console.log(`${secondResult} is greater than ${firstResult}`);
    } else {
        console.log('Both are equal')  
    }
}

getX()