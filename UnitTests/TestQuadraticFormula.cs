using Microsoft.VisualStudio.TestTools.UnitTesting;
using QuadraticFormula;


namespace UnitTests
{
    [TestClass]
    public class TestQuadraticFormula
    {
        [TestMethod]
        public void GetX_Test()
        {
            // Two real roots.
            double expectedRoot = -0.044555558333472335;
            double actualRoot = RealRoots.GetX(15, 68, 3); 
            Assert.AreEqual(expectedRoot, actualRoot);

            // Two Real roots.
            double expectedRoot1 = -1.5417080848653129;
            double actualRoot1 = RealRoots.GetX(1, 45, 67); 
            Assert.AreEqual(expectedRoot1, actualRoot1);

            // Two complex roots. Return -1
            double expectedRoot2 = -1;
            double actualRoot2 = RealRoots.GetX(13, 24, 15);
            Assert.AreEqual(expectedRoot2, actualRoot2);

            // One real root.
            double expectedRoot3 = -2;
            double actualRoot3 = RealRoots.GetX(1, 4, 4);
            Assert.AreEqual(expectedRoot3, actualRoot3);

            // Not a valid quadratic equation. Return -1
            double expectedRoot4 = -1;
            double actualRoot4 = RealRoots.GetX(0, 24, 17);
            Assert.AreEqual(expectedRoot4, actualRoot4);
        }
    }
}
