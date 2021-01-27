import math

if __name__ == '__main__':
    def getX(a, b, c):
        # Global Variables
        # 1st variables in the square root
        sqv1 = b * b
        # 2nd variables in the square root
        sqv2 = 4 * a * c
        # the square root
        sq = math.sqrt(sqv1 - sqv2)
        # Quation denominator
        xDenom = 2 * a
        # X1  Numerator
        x1Num = (-b + sq)
        # X2  Numerator
        x2Num = (-b - sq)

        # positive cal

        x1 = x1Num / xDenom

        #  negative value
        x2 = x2Num / xDenom
        # check largest value of X
        if x1 > x2:
            return x1
        else:
            return x2


    print(f'The largest value of X is : {getX(12, 23, 4)}')
