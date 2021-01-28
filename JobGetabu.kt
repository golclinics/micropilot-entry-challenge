import java.util.*
import java.math.*
import java.text.*

fun main() {
    println(getX())
}

fun getX() : Double {

    val a = 5.0
    val b = 6.0
    val c = 7.0
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
    // check state real and equal roots
    else if (topFormula == 0.0) {
        sRoot = -b / (2 * a)
        fRoot = sRoot

        println("fRoot = ${fRoot.round(2)}")
        println("sRoot = ${sRoot.round(2)}")
        return if(fRoot > sRoot) fRoot else sRoot
    }
    // check state roots are not real
    else {
        val realPart = -b / (2 * a)
        val imaginaryPart = Math.sqrt(-topFormula) / (2 * a)
        
        fRoot = realPart + imaginaryPart
        sRoot = realPart - imaginaryPart

        println("fRoot = ${fRoot.round(2)}")
        println("sRoot = ${sRoot.round(2)}")
        return if(fRoot > sRoot) fRoot else sRoot
    }

}

fun Double.round(decimals: Int = 2): Double = "%.${decimals}f".format(this).toDouble()