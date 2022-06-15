#include <iostream>
using namespace std;
#include <Rcpp.h>
#include <cmath>
using namespace Rcpp;

// [[Rcpp::export]]

class Metropolis
{
public:
  void Metropolis();
  double rnorm(int n, double mean, double sd)
  {
    return exp(((n-mean)^2/2*sd^2))/(sd*sqrt(2*pi));
  }

  double dnorm(int* valArray, double mu, double delta);

  int repeat(int timesRepeat);

  double logPostDensity(double* mu)
  int metroAlgorthm(int timesRepeat2);

  const double PI = 3.1415926535;

private:
  int m_n;
  double m_mean;
  double m_sd;
  int* m_valArray;
  double* m_mu;
  double m_delta;
  int m_df;
  int m_ncp;
  int m_timesRepeat;
  double m_propmu;
  double m_mustar;
}
