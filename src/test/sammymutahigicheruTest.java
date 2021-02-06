import junit.framework.TestCase;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/*
* Makes sure the algorithm does as expected
* */
public class sammymutahigicheruTest{
    private sammymutahigicheru quadratic;
    private final double DELTA = 1e-15;
    @Before
    public void setUp(){
        quadratic = new sammymutahigicheru();
    }
    @Test
    public void firstCaseDetGreaterThanZero_ReturnsMaxRealRoot(){
        Assert.assertEquals(2,quadratic.getX(1,10,-24),DELTA);
    }
}