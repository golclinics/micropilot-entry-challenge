
function getX(a,b,c){
    let discriminant = Math.pow(b,2) - 4*a*c
    if(discriminant < 0){
        return 'X has a complex solution'
    }
    else if(discriminant == 0){
        return 'x1 and x2 are equal' 
    }
    else{
    let x1 = (-b + Math.sqrt(discriminant))/(2*a)
    let x2 = (-b - Math.sqrt(discriminant))/(2*a)

    return Math.max(x1,x2)

    }
}

function testGetX(){
    console.log(getX(9,6,1))
}

//testGetX()