#include <iostream>
using namespace std;
#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]

double rnorm(int n, double mean, double sd)
{
  return std::normal_distribution<double> d(mean, sd);
}
