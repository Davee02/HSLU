t.x <- -10:10
t.x1 <- 0:10

t.y <- t.x^2
t.y1 <- t.x1^2

par(mfrow = c(1, 2))

plot(t.x, t.y)
plot(t.x1, t.y1)

cor(t.x, t.y) # 0 -> Daten liegen symmetrisch zur y-Achse
cor(t.x1, t.y1) # 0.9631427 -> x und y steigen monoton
