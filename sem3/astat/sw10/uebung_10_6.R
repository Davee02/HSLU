mf <- read.csv("./sw10/mannfrau.csv")
diff <- mf$alter.mann - mf$alter.frau
boxplot(diff, col = "orange")

# a)
t.test(mf$alter.mann, mf$alter.frau, alternative = "two.sided", mu = 0, paired = T, conf.level = 0.95)

# b)
t.test(mf$groesse.mann, mf$groesse.frau + 13, alternative = "two.sided", mu = 0, paired = F, conf.level = 0.95)
