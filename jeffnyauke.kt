fun getX(a: Int, b: Int, c: Int): Int {
    val eval = (b * b) - (4 * a * c)
    val sqrt = sqrt(eval.toDouble())
    val x1 = (-b - sqrt) / (2 * a)
    val x2 = (-b + sqrt) / (2 * a)
    return if (x1 > x2) x1.toInt() else x2.toInt()
}