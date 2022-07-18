# Testing my implementation with random test data

source("normalEM.R")

## run on the test data

x = c ( 4.54, 1.57, 1.41, 1.77, 1.43, 0.07, 0.05, 4.19, -0.02, 1.32 )
plot(density(x))

em.out = normalEM(x, 3)

em.out
zapsmall(em.out$z)
colSums(em.out$z)

## another test data set (two normals)

x = c(rnorm(20, mean=-10), rnorm(20, mean=10))
plot(density(x))

em.out = normalEM(x, 2, 5000)

em.out
zapsmall(em.out$z)
colSums(em.out$z)


