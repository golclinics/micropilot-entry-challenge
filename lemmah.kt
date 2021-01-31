import kotlin.math.sqrt

fun getRoots(a: Double, b: Double, c: Double): List<Double> {
    val roots = mutableListOf(0.0, 0.0)
    val determinant = (b * b) - (4 * a * c)
    val squareRoot = sqrt(determinant)

    if (determinant > 0) {
        roots[0] = (-b + squareRoot)/(2 * a)
        roots[1] = (-b - squareRoot)/(2 * a)
    } else if (determinant == 0.0) {
        roots[0] = +(-b + squareRoot)/(2 * a)
    }

    return roots
}

fun getX(a: Double, b: Double, c: Double): Double {
    val roots = getRoots(a, b, c)
    return roots.maxOrNull() as Double
}