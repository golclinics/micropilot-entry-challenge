import Foundation


let a = 5.0

let b = 6.0

let c = 1.0



func getX(_ a:Double, _ b: Double, _ c: Double)->Double?{
    let discriminant = pow(b, 2) - (4*a*c)

    let x1 = (-b + sqrt(discriminant)) / (2*a)
    let x2 = (-b - sqrt(discriminant)) / (2*a)

    if discriminant > 0 || discriminant < 0 {
        return max(x1, x2)
    }
    else{
        print("Since discriminant is less than 0 it will return two complex numbers")
        return nil;
    }
}


if let solution = getX(a, b, c){
    print("Larger solution ", solution)
}