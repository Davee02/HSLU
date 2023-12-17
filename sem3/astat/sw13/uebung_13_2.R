library(ISLR)
library(leaps)

Auto.1 <- within(Auto, rm(name))
reg <- regsubsets(mpg ~ ., data = Auto.1, method = "forward", nvmax = 6)
summary(reg)$which
summary(lm(mpg ~ weight + year, data = Auto.1))

reg <- regsubsets(mpg ~ ., data = Auto.1, method = "backward", nvmax = 6)
summary(reg)$which
summary(lm(mpg ~ weight + year, data = Auto.1))
