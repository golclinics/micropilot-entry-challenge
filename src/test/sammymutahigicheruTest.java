import junit.framework.TestCase;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

/*
* Makes sure the algorithm does as expected
* */
public class sammymutahigicheruTest{
    private sammymutahigicheru quadratic;
    private final double DELTA = 1e-15; //handles off by for double values
    @Before
    public void setUp(){
        quadratic = new sammymutahigicheru();
    }
    @Test
    public void firstCaseDetGreaterThanZero_ReturnsMaxRealRoot(){
        Assert.assertEquals(2,quadratic.getX(1,10,-24),DELTA);
    }
    @Test
    public void secondCaseDeterminantEqualsZero_ReturnGreaterOfTheRoots(){
        Assert.assertEquals(8,quadratic.getX(1,-15,56),DELTA);
    }
    //-2.780776,-0.7192235935955849
    @Test
    public void thirdCaseDeterminantLessThanZero_ReturnsGreaterOfTheTwoNegativeRealNumbers(){
        Assert.assertEquals(-0.7192235935955849,quadratic.getX(2,7,4),DELTA);
    }
    @Test
    public void fakeTest_ReturnsNotEqual(){
        Assert.assertNotEquals(0,quadratic.getX(1,-15,56),DELTA);
    }
}