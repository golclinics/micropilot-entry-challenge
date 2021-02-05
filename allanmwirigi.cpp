#include <iostream>
#include <cmath>
using namespace std;

/*
Given a, b, c for a quadratric expression ax2 + bx + c = 0. Write a function getX that returns the 
larger of the values for X, i.e. if x1 = -2 and x2 = 5, getX should return 5.
*/

double getX(double a, double b, double c) {
  double x1 = ( -b + sqrt(b*b - (4*a*c) ) )/(2*a);
  double x2 = ( -b - sqrt(b*b - (4*a*c) ) )/(2*a);
  if (x1 > x2) {
    return x1;
  }
  else if (x2 > x1) {
    return x2;
  }
  else {
    return x1;
  }
}

int main() {
  cout << getX(6, 11, -35) << endl;
  cout << getX(2, -4, -2) << endl;
  return 0;
}