library(MASS)
attach(Boston)
lm.fit <- lm(medv ~ lstat + age)
summary(lm.fit)

lm.all <- lm(medv ~ ., data = Boston)
summary(lm.all)

lm.cross <- lm(medv ~ lstat * age)
summary(lm.cross)
cor(lstat, age)
