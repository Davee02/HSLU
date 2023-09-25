diet <- read.csv("sw02/Diet.csv")
head(diet)

diet$weight.loss <- diet$weight6weeks - diet$pre.weight
head(diet)

tapply(diet$weight.loss, diet$Diet, mean)
boxplot(weight.loss ~ Diet, data = diet, col = c("red", "green", "blue"))
