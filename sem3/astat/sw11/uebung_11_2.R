library(MASS)

head(Boston)
?Boston
attach(Boston)

lm.fit <- lm(medv ~ lstat)
summary(lm.fit)

names(lm.fit)

coef(lm.fit)

confint(lm.fit)

plot(medv, lstat, col = "blue", pch = 20)
abline(lm.fit, col = "orange", lwd = 3)
