x <- 2:12
p <- c(1,2,3,4,5,6,5,4,3,2,1) / 36

E <- sum(x*p)
E


var.X <- sum((x-E)**2*p)
var.X

stdv.X <- sqrt(var.X)
stdv.X
