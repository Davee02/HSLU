temp1 <- c(39.1, 39.3, 38.9, 40.6, 39.5, 38.4, 38.6, 39.0, 38.6, 39.2)
temp2 <- c(38.1, 38.3 ,38.8, 37.8, 38.2, 37.3, 37.6, 37.8, 37.4, 38.1)

t.test(temp1, temp2, alternative = "greater", mu = 0, paired = F, conf.level = 0.95)
