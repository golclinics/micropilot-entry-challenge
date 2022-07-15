import junit.framework.TestCase.assertEquals
import org.junit.Test

internal class Count_zerosKtTest {

    @Test
    fun countZeros() {
        val arr = intArrayOf(0,1,3,1,0)
        assertEquals(2, countZeros(arr))
    }
}