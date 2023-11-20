z <- c(16.3, 12.7, 14, 53.3, 117, 62.6, 27.6)
b <- c(10.4, 8.91, 11.7, 29.9, 46.3, 25, 29.4)
d <- z - b

mean(d)
sd(d)

t.test(z, b, alternative = "greater", mu = 0, paired = T, conf.level = 0.95)
wilcox.test(z, b, alternative = "greater", mu = 0, paired = T, conf.level = 0.95)
