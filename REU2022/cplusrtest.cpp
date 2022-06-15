#include <iostream>
#include "cplustest.h"
using namespace std;
#include <Rcpp.h>
#include <cmath>
#include <chrono>
#include <random>
using namespace Rcpp;

// [[Rcpp::export]]
  void Metropolis::Metropolis(int n, double mean, double sd, double mu, double delta,
  int df, int ncp, int timesRepeat, int timesRepeat2, double propmu, double mustar)
  {
    m_n = n;
    m_mean = mean;
    m_sd = sd;
    m_valArray = new int[valArray];
    m_mu = new double[mu];
    m_delta = delta;
    m_df = df;
    m_ncp = ncp;
    m_timesRepeat = timesRepeat;
    m_timesRepeat2 = timesRepeat2;
    m_propmu = propmu;
    m_mustar = mustar;
  }

  double Metropolis::rnorm(int n, double mean, double sd)
  {
    int numString[n];
    for (index in n){
      unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
      std::default_random_engine generator (seed);
      std::normal_distribution<double> distribution (mean,sd);
      numString[index].append(distribution(generator));
    }
    return numString;
  }

  double Metropolis::dnorm(int valArray, double mu, double delta)
  {
    return exp(((n-mean)^2/2*sd^2))/(sd*sqrt(2*pi));
  }

  int Metropolis::repeat(int timesRepeat)
  {
    for (index = 0; index <= timesRepeat; ++index)
    {
      postMatrix[index] = rnorm(n,mean,sd);
    }
    return postMatrix;
  }

  double Metropolis::logPostDensity(double mu)
  {
    return log(Rcpp::dt(mu,df,ncp)) + sum(log(dnorm(valArray,mu,delta)));
  }

  int Metropolis::metroAlgorthm(int timesRepeat2)
  {
    bool r;
    double u;
    for (index in (timesRepeat2 - 1))
    {
      propmu = rnorm(n,mu[index],delta);
      mustar = logPostDensity(propmu)-logPostDensity(mu[index]);
      r = min(1,exp(mustar));
      u = Rcpp::runif(10, 0.0, 1.0);
      if (u<r)
      {
        mu[index+1] = propmu;
      } else
      {
        mu[index+1] = mu[index];
      }

    }


  }
