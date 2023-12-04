library(ISLR)

pairs(Auto)

head(Auto)
Auto.1 <- within(Auto, rm(name))
head(Auto.1)
cor(Auto.1)

lm.all <- lm(mpg ~ ., data = Auto.1)
summary(lm.all)

lm.cross <- lm(mpg ~ weight * year, data = Auto.1)
summary(lm.cross)
