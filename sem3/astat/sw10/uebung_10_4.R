x <- c(186, 181, 176, 149, 184, 190, 158, 139, 175, 148, 152, 111, 141, 153, 190, 157, 131, 149, 135, 132)
y <- c(129, 132, 102, 106, 94, 102, 87, 99, 170, 113, 135, 142, 86, 143, 152, 146, 144)

mean(x)
mean(y)

wilcox.test(x, y, alternative = "two.sided", mu = 0, paired = F,conf.level = 0.95)
