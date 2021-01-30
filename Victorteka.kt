import kotlin.math.max
import kotlin.math.sqrt

fun getX(a: Int, b: Int, c: Int):Double{
    val inSideSqrt = (b * b)-(4 * a * c)
    val x1 = (-b + sqrt(inSideSqrt.toDouble())) / (2*a)
    val x2 = (-b - sqrt(inSideSqrt.toDouble())) / (2*a)
    return max(x1, x2)
}

fun main(){
    //text 5x2 + 6x + 1 = 0
    println("Max value of x ${getX(5, 6, 1)}")
}