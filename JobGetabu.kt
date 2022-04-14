import java.util.*
import java.math.*
import java.text.*

fun main() {
    println(getX())
}

fun getX(a: int, b: int, c: int) : Double {

    val fRoot: Double
    val sRoot: Double

    val topFormula = b * b - 4.0 * a * c
    
    // check state real and different roots
    if (topFormula > 0) {
        fRoot = (-b + Math.sqrt(topFormula)) / (2 * a)
        sRoot = (-b - Math.sqrt(topFormula)) / (2 * a)

        println("fRoot = ${fRoot.round(2)}")
        println("sRoot = ${sRoot.round(2)}")
        
        return if(fRoot > sRoot) fRoot else sRoot
    }
}

fun Double.round(decimals: Int = 2): Double = "%.${decimals}f".format(this).toDouble()
