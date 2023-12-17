library(ISLR)
head(Carseats)
?Carseats

summary(lm(Carseats$Sales ~ Carseats$Price + Carseats$Urban + Carseats$US))

summary(lm(Carseats$Sales ~ Carseats$Price + Carseats$US))
