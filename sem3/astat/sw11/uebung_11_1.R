library(ISLR)

head(Auto)
?Auto

model <- lm(Auto$mpg ~ Auto$horsepower)
summary(model)
confint(model)

plot(Auto$horsepower, Auto$mpg, col = "blue", pch = 20)
abline(model, col = "orange", lwd = 3)

