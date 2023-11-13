# a)
signiv <- 0.05
qnorm(p=signiv, mean=50, sd=3/sqrt(16))

x <- c(46, 48, 52, 49, 46, 51, 52, 47, 49, 44, 48, 51, 49, 50, 53, 47)
mean(x)

# ODER
pnorm(q=mean(x), mean=50, sd=3/sqrt(16))

# b)
pnorm(q=mean(x), mean=50, sd=3/sqrt(100))

# c)
t.test(x, mu=50, alternative = "less")
