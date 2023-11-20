a <- c(120, 265, 157, 187, 219, 288, 156, 205, 163)
b <- c(127, 281, 160, 185, 220, 298, 167, 203, 171)

t.test(a, b, alternative = "less", mu = 0, paired = TRUE, conf.level = 0.95)
