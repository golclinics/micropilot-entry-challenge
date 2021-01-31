fun getX(a: Double, b: Double, c: Double): Double{

    var root1: Double = 0.0
    var root2: Double = 0.0
    val determinant: Double = (b * b - 4 * a * c)
    if(determinant>0){
        root1 = (-b + Math.sqrt(determinant)) / (2 * a)
        root2 = (-b - Math.sqrt(determinant)) / (2 * a)

    }else if(determinant == 0.0){
        root1 = -b / (2 * a)
        root2 = root1

    }

    return max(root1, root2)

}