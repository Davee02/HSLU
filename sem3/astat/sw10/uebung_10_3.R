jackals <- read.table(file = "./sw10/jackals.txt", header = TRUE)
t.test(jackals[, "M"], jackals[, "W"], mu = 0, paired = F, conf.level = 0.95)
wilcox.test(jackals[, "M"], jackals[, "W"], alternative = "two.sided", mu = 0, paired = F,conf.level = 0.95)
