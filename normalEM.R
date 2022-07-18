# Below is my implementation of the EM algorithm


# EM algorithm for fitting mixture of K one-dimensional normal distributions

normalEM = function (x, K, numRepeats=100)
{ 
  # total number of samples
  ntot = length(x)

  # initialise z randomly
  z = matrix(runif(K*ntot, 0.5, 1), ntot, K)
  # make rows add up to 1
  rowStd = function(z) sweep(z, 1, rowSums(z), "/")
  z = rowStd(z)
  
  m = numeric(K) # centroid means
  s2 = numeric(K) # variances

  # start EM algorithm
  for (r in 1:numRepeats)
  {
    # Alternate between M and E steps:

    # M: maximise expected log likelihood to get new model parameters
    # we use the analytic expressions
    n = colSums(z)
    pi = n / ntot  # estimated frequencies
    for (k in 1:K) 
    {
      m[k] = sum(z[,k]*x) / n[k] # estimated centroids
      s2[k] = sum(z[,k]*(x-m[k])^2) / n[k] # estimated variances
     }

    # E: compute the probabilities z[i,k] of sample i to be in class k
    for (i in 1:ntot)
       z[i,] = pi * dnorm(x[i], mean=m, sd=sqrt(s2))
    z = rowStd(z)
  }

  return( list(pi=pi, m=m, s2=s2, z=z) )
}
