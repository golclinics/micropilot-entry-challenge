fun main() {
    val arr = intArrayOf(0,1,3,1,0)
    countZeros(arr)
}

fun countZeros(arr: IntArray): Int {
    var count = 0
    for (i in arr) {
        if (i == 0) {
            count++
        }
    }
    println(count)
    return count
}
