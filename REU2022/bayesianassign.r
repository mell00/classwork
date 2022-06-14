#3
n = 5
xbar = 10
sigma = 2
theta = 12
tau = 3
matrix = NA

postmean = function(n,xbar,sigma,theta,tau){ #calculate posterior mean
  (n*xbar*tau^2+sigma^2*theta)/(n*tau^2+sigma^2)
}
postsd = function(n,xbar,sigma,theta,tau){ #calculate posterior standard deviation
   sqrt((sigma^2*tau^2)/(n*tau^2*sigma^2))
}
posterior = function(n,postmean,postsd){ #generate random normal distribution 1 time
   rnorm(n,mean=postmean,sd=postsd)
}
keepgoing = function(n,postmean,postsd){ #generate random normal distribution 10000 times
  for (i in 1:10000){
    matrix[i] = rnorm(1,mean=postmean,sd=postsd)
  }
  matrix
}


print(postmean(n,xbar,sigma,theta,tau)) #print posterior mean
print(postsd(n,xbar,sigma,theta,tau)) #print posterior standard distribution
print(posterior(n,postmean(n,xbar,sigma,theta,tau),postsd(n,xbar,sigma,theta,tau))) #print 1 random normal distribution
plot(print(keepgoing(n,postmean(n,xbar,sigma,theta,tau),postsd(n,xbar,sigma,theta,tau)),xlim=c(0,20000),ylim=c(0,20000))) #plot 10000 random normal distribution points
hist(print(keepgoing(n,postmean(n,xbar,sigma,theta,tau),postsd(n,xbar,sigma,theta,tau)),xlim=c(0,20000),ylim=c(0,20000)))
#----------------------------------------------------
#(d)
m=10000
mu = c(20)
delta = 0.1
ncp = theta
df = n - 1 #degrees of freedom
x = NA
newmatrix = NA

for (i in 1:5){ #assign 5 positive even integers
  x[i] = 2*i
}
print(x)
logpostdensity <- function(mu) {
  log(dt(mu, df,ncp)) + sum(log(dnorm(x, mu, sigma)))
}

for (i in 1:(m-1)) { #run Metropolis algorithm
  propmu = rnorm(1,mean=mu[i],sd=delta)
  mustar = logpostdensity(propmu)-logpostdensity(mu[i])
  r = min(1,exp(mustar))
  u = runif(1,min=0,max=1)
  if (u<r) {
    mu[i+1] = propmu}
  else {mu[i+1] = mu[i]}
}

for (i in 1:m) {
  newmatrix[i]=rnorm(m,mean=propmu,sd=delta)
}
plot(print(newmatrix))
hist(print(newmatrix))
acf(mu)


#4
n = 5
xbar = 10
sigma = 2
theta = 11
tau = 3
matrix = NA

postmean = function(n,xbar,sigma,theta,tau){ #calculate posterior mean
  (n*xbar*tau^2+sigma^2*theta)/(n*tau^2+sigma^2)
}
postsd = function(n,xbar,sigma,theta,tau){ #calculate posterior standard deviation
  sqrt((sigma^2*tau^2)/(n*tau^2*sigma^2))
}
posterior = function(n,postmean,postsd){ #generate random normal distribution 1 time
  rnorm(n,mean=postmean,sd=postsd)
}
keepgoing = function(n,postmean,postsd){ #generate random normal distribution 10000 times
  for (i in 1:10000){
    matrix[i] = rnorm(n,mean=postmean,sd=postsd)
  }
  matrix
}


print(postmean(n,xbar,sigma,theta,tau)) #print posterior mean
print(postsd(n,xbar,sigma,theta,tau)) #print posterior standard distribution
print(posterior(n,postmean(n,xbar,sigma,theta,tau),postsd(n,xbar,sigma,theta,tau))) #print 1 random normal distribution
plot(print(keepgoing(n,postmean(n,xbar,sigma,theta,tau),postsd(n,xbar,sigma,theta,tau)),xlim=c(0,20000),ylim=c(0,20000))) #plot 10000 random normal distribution points
#----------------------------------------------------
#(d)
m=10000
mu = c(10000)
delta = 0.1
df = 9 #degrees of freedom
x = NA
newmatrix = NA

for (i in 1:5){ #assign 5 positive even integers
  x[i] = 2*i
}
print(x)
postdensity <- function(mu) {
  dt(mu, df) * prod(dt(x, df, mu))
}

for (i in 1:(m-1)) { #run Metropolis algorithm
  propmu = rnorm(1)
  r = postdensity(propmu)/postdensity(mu[i])
  acceptmu = rbinom(1, 1, min(1,r))
  mu[i+1] = if (acceptmu) propmu else mu[i]
}

for (i in 1:m) {
  newmatrix[i]=rnorm(m,mean=propmu,sd=delta)
}
plot(print(newmatrix))
hist(print(newmatrix))
