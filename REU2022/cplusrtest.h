#include <iostream>
using namespace std;
#include <Rcpp.h>
#include <cmath>
using namespace Rcpp;

// [[Rcpp::export]]

class Metropolis
{
public:
  double rnorm(int n, double mean, double sd)
  {
    return exp(((n-mean)^2/2*sd^2))/(sd*sqrt(2*pi));
  }

  int repeat(int timesRepeat,int &postMatrixmatrix)

  int metroAlgorthm(int timesRepeat2)

private:
  int n;
  double mean;
  double sd;
  double mu;
  double delta;
  int df;
  int ncp;
  int timesRepeat;
  int &postMatrix;
  int &newPostMatrix;
  double propmu;
  double mustar;
}
